from django.db import models
from django.core.validators import RegexValidator
from django import forms

# Create your models here.
class User(models.Model):
    GENDER_OPTIONS = [('Male','Male'),('Female','Female')] #tuples of (actual value, human readable name)
    phone = models.BigIntegerField(validators=[RegexValidator(regex='^[0-9]{10}$', message='Length has to be 10')], blank = False, primary_key = True)
    password = models.CharField(max_length=100, blank = False)
    name = models.CharField(max_length = 50, blank = False)
    email = models.EmailField(max_length = 200, blank = True)
    earning = models.PositiveIntegerField(default=0 ,blank = False)
    gender = models.CharField(max_length=6,choices=GENDER_OPTIONS,blank=True)

    def __str__(self):
        return (str(self.phone))

class Referal(models.Model):
    refid = models.CharField(max_length = 10, blank = False, primary_key = True)
    user1 = models.ForeignKey(User, blank = False, on_delete = models.SET_NULL, null = True, related_name='user1')
    user2 = models.ForeignKey(User, blank = False, on_delete = models.SET_NULL, null = True, related_name='user2')
    date = models.DateField(auto_now_add=True, blank = False)
    status = models.CharField(max_length = 20, blank = False)
    reward = models.PositiveIntegerField(blank = False)

    def __str__(self):
        return (self.refid)

class Store(models.Model):
    name = models.CharField(max_length = 10, blank = False, primary_key = True)
    total_orders = models.PositiveIntegerField(default=0, blank = False)
    payment_threshold_period = models.PositiveIntegerField(blank = True,null =True)

    def __str__(self):
        return (self.name)

class Product(models.Model):
    pid = models.CharField(max_length = 10, blank = False, primary_key = True)
    title = models.CharField(max_length = 50, blank = False)
    price = models.PositiveIntegerField(blank = False)
    discount = models.PositiveIntegerField(blank = False)
    cashback = models.PositiveIntegerField(blank = False)
    rating = models.PositiveIntegerField(blank = False)
    specs = models.CharField(max_length = 300, blank = False)
    link = models.URLField(blank = False)

    def __str__(self):
        return (self.pid)

class Order(models.Model):
    oid = models.CharField(max_length = 10, blank = False, primary_key = True)
    user = models.ForeignKey(User, blank = False, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True, blank = False)
    amount = models.PositiveIntegerField(blank = False)
    cashback = models.PositiveIntegerField(blank = False)
    status = models.CharField(max_length = 20, blank = False)
    store = models.ForeignKey(Store, blank=True, on_delete=models.SET_NULL, null = True)
    product = models.ForeignKey(Product, blank=True, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return (self.oid)

class Offer(models.Model):
    oid = models.CharField(max_length = 10, blank = False, primary_key = True)
    category = models.CharField(max_length = 20, blank = False)
    cashback = models.PositiveIntegerField(blank = False)
    link = models.URLField(blank = False)
    title = models.CharField(max_length = 50, blank = False)
    terms = models.CharField(max_length = 300, blank = False)
    store = models.ForeignKey(Store, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return (self.oid)
