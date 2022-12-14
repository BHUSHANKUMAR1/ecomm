from django.db import models
import datetime
# Create your models here.


class Signup(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    mobile_no = models.BigIntegerField()
    gender = models.CharField(max_length=20)
    #a = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Category(models.Model):
    name = models.CharField(max_length=20)
    cat_image = models.ImageField(upload_to='upload/category/')

    def __str__(self):
        return self.name


class Product(models.Model):
    pro_name = models.CharField(max_length=20)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)
    pro_image = models.ImageField(upload_to='upload/category/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pro_name


class Order(models.Model):
    address = models.TextField(max_length=400, null=True)
    mobile_no = models.BigIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Signup, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.first_name


class Table(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)
    fav = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.first


