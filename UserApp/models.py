from django.db import models
from AdminApp.models import*

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email= models.EmailField()
    phone= models.IntegerField()
    message=models.TextField()

class Register(models.Model):
    username=models.CharField(max_length=30)
    password=models.TextField()
    email= models.EmailField()
    mobile=models.IntegerField()

class Cart(models.Model):
    usercart=models.ForeignKey(Register,on_delete=models.CASCADE)
    userpro=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0)

class Checkout(models.Model):
    usercheckout=models.ForeignKey(Register,on_delete=models.CASCADE)
    usercart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    address=models.TextField()
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    pincode=models.IntegerField()