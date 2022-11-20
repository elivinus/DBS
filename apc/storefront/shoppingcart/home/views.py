
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ..authentication.models import MenuItem
from ..authentication.forms import CreateNewList
from ..authentication.models import ItemList, Item

# Create your views here.

def all_menu(request):
	menu_test = MenuItem.objects.all()
	return render(request, 'accounts/menu.html', {'menu':menu_test})
	


def say_hello(request):
	return render(request,'home/homepage.html', { 'pagename' : 'home'})

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
	return render(request,'accounts/register.html', {'form':form})

def login_request(request):
    
    return render(request,'accounts/login.html', {'form':'login'})

# class page request
class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/index.html')

class About(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/about.html')

class Menu(View):
	def get(self, request, *args, **kwargs):
		return render(request,
		'menu.html', {
		"name": name,
		"price": price,
		"allergies": allergies,
		})

class Contact(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/contact.html')

class Gallery(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/gallery.html')

