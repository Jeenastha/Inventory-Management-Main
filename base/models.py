from django.db import models
from django.contrib.auth.models import AbstractUser  

# Create your models here.    
class User(AbstractUser):
    username=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    contact=models.BigIntegerField(null=True)
    location=models.CharField(max_length=200)
    image=models.ImageField(null=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

class ProductType(models.Model):
    name=models.CharField(max_length=200)

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    size=models.CharField(max_length=200,null=True)
    quantity=models.IntegerField()
    price=models.FloatField() 
    department=models.ManyToManyField('Department',null=True)
    type=models.ForeignKey(ProductType,on_delete=models.SET_NULL,null=True)   

class Purchase(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField() 
    quantity=models.IntegerField()
    supplier=models.ForeignKey('Supplier',on_delete=models.CASCADE)

class Supplier(models.Model):
    name=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    location=models.CharField(max_length=200)
    email=models.EmailField()

class Department(models.Model):
    name=models.CharField(max_length=200)
    floor=models.IntegerField()
    description=models.TextField()        

