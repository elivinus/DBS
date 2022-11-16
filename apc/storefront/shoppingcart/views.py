
from django.http import HttpResponse
from django.shortcuts import render

from .forms import CreateNewList

# Create your views here.

def say_hello(request):
	return render(request,'homepage.html', { 'pagename' : 'home'})

def register_request(request):
    form = CreateNewList()
    return render(request,'register.html', {'form':form})

def login_request(request):
    
    return render(request,'login.html', {'form':'login'})