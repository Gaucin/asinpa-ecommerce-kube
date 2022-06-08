from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', "username"]

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Customer(models.Model):
    name = models.CharField(max_length=80)
    contact_name = models.CharField(max_length=80)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.contact_name}"


class Employee(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    birth_date = models.DateField()
    photo = models.ImageField()
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Shipper(models.Model):
    name = models.CharField(max_length=80)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.phone}"
