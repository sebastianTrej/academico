from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    dni = models.CharField(max_length=10, default='')