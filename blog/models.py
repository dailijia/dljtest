from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    create_date = models.DateField(auto_now = True)
    modify_date = models.DateField(auto_now = True)
    context = models.TextField()
    is_show = models.BooleanField()

    class Meta:
        db_table = "ariticle"

    def __str__(self):
        return self.title

class MyUser(AbstractBaseUser):
    """docstring for ClassName"""
    identifier = models.CharField(max_length=40,unique = True)
    USERNAME_FIELD = 'identifier'

    class Meta:
        db_table='MyUser'

    def __str__(self):
        return self.USERNAME_FIELDS
        
        
