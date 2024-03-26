from django.contrib.auth.models import AbstractUser
from django.db import models
from mainApp.models import *

class Profile(AbstractUser):
    phone_number=models.CharField(max_length=20, unique=True)
    gender=models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    birth_date=models.DateField(null=True, blank=True)
    countr=models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city=models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.username

