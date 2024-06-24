from django.contrib.auth.models import AbstractUser
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
    
class Asset_login(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100) 
    position = models.CharField(max_length=50) 

    def _str_(self):
        return self.username    
    
class AssetTable(models.Model):
    Asset_name = models.CharField(max_length=100)
    Asset_type = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Item_code= models.CharField(max_length=100)
    Assigned_To = models.CharField(max_length=100)
    images=models.ImageField(blank=True)