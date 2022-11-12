from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def calculate():
	x = 1
	y = 2 
	return x

def say_hello(request):
	x =  calculate()
	y = 2
#	return HttpResponse ('Home Page!')
	return render(request,'homepage.html', { 'pagename' : 'Livinus'})
