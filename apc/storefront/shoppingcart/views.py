
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import CreateNewList
from .models import ItemList, Item

# Create your views here.

def say_hello(request):
	return render(request,'homepage.html', { 'pagename' : 'home'})

def register_request(request):
    
	if request.method =='POST':
		form = CreateNewList(request.POST)
		if form.is_valid():
			itemName = form.cleaned_data['name']
			createItem = ItemList(name=itemName)
			createItem.save
			print("Item Created Successfully!")
	#	return HttpResponseRedirect("/%i" %createItem.id)
	else:
		form = CreateNewList()
	return render(request,'register.html', {'form':form})

def login_request(request):
    
    return render(request,'login.html', {'form':'login'})

# class page request
class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'index.html')

class About(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'about.html')

class Menu(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'menu.html')

class Contact(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'contact.html')

class Gallery(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'gallery.html')

