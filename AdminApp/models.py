from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images',default='null.jpg')

class Product(models.Model):
    name=models.CharField(max_length=40)
    description=models.TextField()
    category=models.CharField(max_length=20)
    price=models.ImageField()
    image=models.ImageField(upload_to='images',default='null.jpg')