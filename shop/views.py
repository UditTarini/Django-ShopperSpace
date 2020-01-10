from django.shortcuts import render
from django.http import HttpResponse
from .models import product, Contact, Orders
from math import ceil
from django.contrib import messages 
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

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
    return render(request, 'shop/index.html', params)
    
def cart(request):
    return render(request, 'shop/cart.html')

def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def productView(request, prodid):
    prodView = product.objects.filter(id=prodid)
    return render(request, 'shop/productview.html', {'prodView':prodView[0], 'i':prodid})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
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
                       address1=address1, address2=address2)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'shop/checkout.html') 