from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib
# Create your views here.
from django.http import HttpResponse

def testing(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'index1.html')