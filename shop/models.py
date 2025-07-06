from django.db import models

# Create your models here.
class Products(models.Model):
    title =models.CharField(max_length=255)
    price =models.FloatField(max_length=255)
    discount_price =models.FloatField(max_length=255)
    category =models.CharField(max_length=255)
    product_description = models.TextField(max_length=255)
    image = models.CharField(max_length=300)

class Order(models.Model):
    items= models.CharField(max_length=1000)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)

