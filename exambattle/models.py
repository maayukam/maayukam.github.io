from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=15,unique=True)
    last_name = models.CharField(max_length=50,blank=True)

class Question(models.Model):
    question = models.CharField(max_length = 255)
    ans1     = models.CharField(max_length=255,blank=True)
    ans2     = models.CharField(max_length=255,blank=True)
    ans3 = models.CharField(max_length=255,blank=True)
    ans4 = models.CharField(max_length=255,blank=True)
    answer = models.CharField(max_length=255,blank=True)
    # def __str__(self):
    #     return self.Question