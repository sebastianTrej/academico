from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    status = models.BooleanField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)

class Students(models.Model):
    code = models.CharField(max_length=100)
    id_person = models.IntegerField(null=False)
    status = models.BooleanField(null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)

class identification_types(models.Model):
    name = models.CharField(max_length=50, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)

class cities(models.Model):
    name = models.CharField(max_length=110, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=10, null=False)
    id_dept = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)

class persons(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_exp_city  = models.ForeignKey(cities, on_delete=models.CASCADE)
    firs_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=50, null=False)
    id_ident_type = models.IntegerField(null=False)
    ident_number = models.CharField(max_length=15, null=False)
    id_exp_city = models.IntegerField(null=False)
    address = models.CharField(max_length=150, null=False)
    mobile = models.CharField(max_length=50, null=False)
    id_user = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)

class departaments(models.Model):
    name = models.CharField(max_length=100, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=10, null=False)
    id_country = models.IntegerField(null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)

class countries(models.Model):
    name = models.CharField(max_length=100, null=False)
    abrev = models.CharField(max_length=10, null=False)
    descrip = models.CharField(max_length=10, null=False)
    created_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    updated_at = models.DateTimeField(default=datetime.datetime.now, null=False)
    deleted_at = models.DateTimeField(null=True)