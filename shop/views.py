from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact, Orders, OrderStatus
from math import ceil
from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
from django.http import HttpResponse

MERCHANT_KEY = 'm key'


def home(request):
      trendProd = product.objects.filter(label="Trending")
      newProd = product.objects.filter(label="New")
     
      params = {'trendProducts':trendProd, 'newProducts' :newProd }
    
      return render(request, 'home.html',params)
   



def catagoryView(request, cat):

    prod = product.objects.filter(slug=cat)
    params = {'products':prod}
    return render(request, 'catagoryview.html',params)

def search(request):
    
    query = request.GET.get('search')
    products = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prods = product.objects.filter(category=cat)
      
        prod = [item for item in prods if matchSearch(query, item)]
        if len(prod) != 0:
           
            products.append(prod)    
    params = {'products': products[0], "msg": ""}
    if len(products) == 0 or len(query)<3:
        params = {'msg': "Please enter a valid search query"}
    
   
    return render(request, 'search.html', params)

def index(request): 
    allProds = []
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds}
    return render(request, 'index.html', params)

@login_required(login_url="/accounts/login")    
def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')

def matchSearch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.productName.lower() or query in item.category.lower():
        return True
    else:
        return False


def productView(request, prodid, cat):
    prodView = product.objects.filter(id=prodid)
     
    relatedProd = product.objects.filter(slug=cat)

    return render(request, 'productview.html', {'prodView':prodView[0], 'i':prodid, 'relatedProd':relatedProd })

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount','')
        firstName = request.POST.get('firstName', '')
        lastName = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip_code', '')
        address1 = request.POST.get('address1', '') 
        address2 = request.POST.get('address2', '') 
        order = Orders(items_json=items_json, firstName=firstName,lastName=lastName,
                       email=email,phone=phone,country=country,
                       state=state,city=city,zip_code=zip_code,
                       address1=address1, address2=address2, amount=amount)
        order.save()
        thank = True
        id = order.order_id
        param_dict = {

                'MID': 'm id',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/paymentstatus/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})
    return render(request, 'checkout.html') 

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            
           print("order")
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        try:
            order = Orders.objects.filter(order_id=orderId)
            if len(order)>0:
                status = OrderStatus.objects.filter(order_id=orderId)
                updates = []
                for item in status:
                    updates.append({'text': item.status_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success","updates":updates, "jsonItem":order[0].items_json}, default=str)
                    
                return HttpResponse(response)
                
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'tracker.html')    