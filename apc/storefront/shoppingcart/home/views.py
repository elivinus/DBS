
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from ..authentication.models import MenuItem
from ..authentication.forms import CreateNewCustomer
from ..authentication.models import Customer, OrderDetail
from ..authentication.models import Category, Order


# Create your views here.


def say_hello(request):
	return render(request,'home/homepage.html', { 'pagename' : 'home'})

def register_request(request):
    
	if request.method =='POST':
		form = CreateNewCustomer(request.POST)
		if form.is_valid():
			itemName = form.cleaned_data['name']
			createItem = Customer(name=itemName)
			createItem.save
			print("Item Created Successfully!")
	#	return HttpResponseRedirect("/%i" %createItem.id)
	else:
		form = CreateNewCustomer()
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

class Cart(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'accounts/cart.html')

class Login(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'accounts/login.html')

class Signup(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'accounts/register.html')

class Menu(View):
	def get(self, request, *args, **kwargs):	
		starters = MenuItem.objects.filter(category__name__contains='Starters')
		mains = MenuItem.objects.filter(category__name__contains='Main')
		vegetarian = MenuItem.objects.filter(category__name__contains='Vegetarian')
		noodles = MenuItem.objects.filter(category__name__contains='Noodles')
		softdrinks = MenuItem.objects.filter(category__name__contains='Soft Drinks')
		wine = MenuItem.objects.filter(category__name='Wine')
		softdrinks = MenuItem.objects.filter(category__name__contains='soft')
		# pass into context
		contect = {
			'starters': starters,
			'mains': mains,
			'noodels': noodles,
			'vegetarian': vegetarian,
			'softdrinks': softdrinks,
			'wine': wine,
		}
		return render(request, 'accounts/menu.html', contect)

	  
class Order(View):
    def get(self, request, *args, **kwargs):
        drinks = MenuItem.objects.filter(category__name__contains('drinks'))
        appetizer = MenuItem.objects.filter(category__name__contains('appetizer'))
        fries = MenuItem.objects.filter(category__name__contains('fries'))
    

class Contact(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/contact.html')

class Gallery(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/gallery.html')

