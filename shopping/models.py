from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class product(models.Model):
    productname=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images')
    qty=models.IntegerField()

class cartitem(models.Model):
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    image=models.ImageField(upload_to='images')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    House_no =models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    pincode = models.IntegerField()
    city =models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    contactno = models.IntegerField()

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(product, on_delete=models.CASCADE)
    address = models.ForeignKey(address, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()


