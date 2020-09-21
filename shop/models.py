from django.db import models
from django.conf import settings
from datetime import datetime 
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify


from allauth.account.forms import SignupForm

# Create your models here.

LABEL = (
    ('Trending', 'Trending'),
    ('New','New'),
    ('50%','50%'),
    )

    
class product(models.Model):

    productId = models.AutoField
    productName = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    publishDate = models.DateField()
    image = models.CharField(max_length=800)
    price = models.CharField(max_length=15)
    oldPrice = models.CharField(max_length=15, blank=True)
    category = models.CharField(max_length=50,default="")
    subCatagory = models.CharField(max_length=50,default="")
    label = models.CharField(max_length=16, choices=LABEL, default='New')
    slug = models.SlugField(max_length=100,null=True,blank=True,unique=False)

    def __str__(self):
        return self.productName

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.category)

pre_save.connect(slug_generator, sender=product)     

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name  

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    firstName = models.CharField(max_length=90)
    lastName = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=111, default="")           
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)

STATUS = (
    ('Order Confirmed', 'order confirmed'),
    ('Order Processing','order processing'),
    ('Shipped','shipped'),
    ('On The Way' ,'on the Way'),
    ('Delivered','Delivered'),)

class OrderStatus(models.Model):
    status_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    status_desc = models.CharField(max_length=16, choices=STATUS, default='Order Confirmed')
    timestamp = models.DateField(auto_now_add=True)

     
    
    