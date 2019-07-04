from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name=models.CharField(max_length=50,primary_key=True,verbose_name='')
    title=models.CharField(max_length=50,verbose_name='')
    description=models.TextField(default='',verbose_name='')
    image=models.ImageField(null=True)
    parent=models.ForeignKey('ProductCategory',null=True,on_delete=models.SET_NULL)

class Product(models.Model):
    name=models.CharField(primary_key=True,max_length=50,verbose_name='')
    title=models.CharField(max_length=50,verbose_name='')
    image=models.ImageField(null=True)
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,verbose_name='')

class User(models.Model):
    telephone=models.CharField(max_length=20,primary_key=True)
    nick_name=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    salt=models.CharField(max_length=100)