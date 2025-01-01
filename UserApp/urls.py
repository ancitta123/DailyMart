from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
   path('user',views.userindex,name='userindex'),
   path('cardc',views.categorycard,name='categorycard'),
   path('productcard/<str:cat>',views.productcard,name='productcard'),
   path('singleproduct/<int:id>',views.singleproduct,name='singleproduct'),
   path('home',views.home,name='home'),
   path('contact',views.contact,name='contact'),
   path('contactdata',views.contactdata,name='contactdata'),
   path('abouts',views.abouts,name='abouts'),
   path('login',views.login,name='login'),
   path('register',views.register,name='register'),
   path('registerdata',views.registerdata,name='registerdata'),
   path('publicdata',views.publicdata,name='publicdata'),
   path('userlogout',views.userlogout,name='userlogout'),
   path('cart',views.cart,name='cart'),
   path('checkout',views.checkout,name='checkout'),
   path('addtocart/<int:id>',views.addtocart,name='addtocart'),
   path('deletecart/<int:id>',views.deletecart,name='deletecart'),
   path('checkoutdata',views.checkoutdata,name='checkoutdata'),
   path('success',views.success,name='success')
]