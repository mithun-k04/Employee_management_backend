from django.db import models
# Create your models here.

class Hradmin(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    
class Employee(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    department = models.CharField(max_length=100, blank=False)
    designation = models.CharField(max_length=100, blank=False)
    join_date = models.DateField()