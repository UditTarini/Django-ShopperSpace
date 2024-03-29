from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ShopHome'),
    path('home/', views.home, name='home'),
    path('shop/', views.home, name='home'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrackingStaus'),
    path('search/', views.search, name='Search'),
    path('product/<slug:cat>/<int:prodid>',
         views.productView, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
    path('cart/', views.cart, name='Cart'),
    path("paymentstatus/", views.handlerequest, name="PaymentStatus"),
    path('<slug:cat>/', views.catagoryView, name='catagoryView'),
    path('sales/<slug:sale>/', views.salesView, name='salesView'),


]
