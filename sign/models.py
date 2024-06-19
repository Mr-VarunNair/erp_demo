#from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#class Asset_Login(AbstractUser):
from django.db import models
'''
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100) 
    position = models.CharField(max_length=50) 

    def _str_(self):
        return self.username 
'''
class CustomUser(AbstractUser):
    position = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username   