from operator import mod
from django.db import models


class Category(models.Model):
    description = models.CharField(max_length=70)


class Product(models.Model):
    name = models.TextField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.CharField(max_length=80)
    price = models.IntegerField()
