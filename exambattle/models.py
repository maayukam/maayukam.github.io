from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=15,unique=True)