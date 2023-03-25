from django.db import models
from django.contrib import auth
class User(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    mnum=models.CharField(max_length=12)
    pwd=models.CharField(max_length=8)
def __str__(self):
    return self.name
  
    
    