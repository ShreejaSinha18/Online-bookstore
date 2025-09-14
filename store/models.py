from django.db import models

# Create your models here.

class customer(models.Model):
    uname=models.CharField(max_length=15)
    pwd=models.CharField(max_length=8)
    rpwd=models.CharField(max_length=8)
    class Meta:
        db_table="customer"

class author(models.Model):
    name=models.CharField(max_length=50)
    class Meta:
        db_table="author"

class books(models.Model):
    bname=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()
    class Meta:
        db_table="books"

class cart(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    cost=models.IntegerField()
    class Meta:
        db_table="cart"

class buyer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    date=models.CharField(max_length=10)
    mode=models.CharField(max_length=50)
    class Meta:
        db_table="buyer"