from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login,authenticate
from exambattle.forms import SignUpForm
# Create your views here
from django.http import HttpResponse
import datetime
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})