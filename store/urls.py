from django.urls import path
from django.conf.urls import include
from django.contrib import admin

from . import views

urlpatterns = [
        #Leave as empty string for base url
    path('cakes/' , views.cakes,name="cakes") ,   
    path('bouquets/' , views.bouquets,name="bouquets") ,   
    path('gifts/' , views.gifts,name="gifts") ,   
    path('seasonal/' , views.seasonal,name="seasonal") ,   
    path('covid/' , views.covid,name="covid") ,   
    path('index/', views.indexPage,name="index"),
    path('logout',views.logoutUser,name="logout"),
  	path('login/', views.loginPage,name="login"), 
  	path('register/', views.registerPage,name="register"),
   	path('sign_cust/', views.signcust,name="sign_cust"),     
  	path('signsell1/', views.signsell1,name="signsell1"),     
    path('signsell2/', views.signsell2,name="signsell2"),     
  	path('index/', views.indexPage, name="index"),
    path('',views.store,name="store"),
  	path('cart/', views.cart, name="cart"),
  	path('checkout/', views.checkout, name="checkout"),
  	path('update_item/', views.updateItem, name="update_item"),
  	path('process_order/', views.processOrder, name="process_order"),

]