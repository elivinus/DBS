
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from ..authentication.models import MenuItem
from ..authentication.forms import CreateNewCustomer
from ..authentication.models import Customer, OrderDetail
from ..authentication.models import Category, Order
from ..authentication.models import Order, OrderDetail
from django.contrib.auth import login, authenticate

import json



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
	return render(request,'accounts/signup.html', {'form':form})

def login_request(request):
    
    return render(request,'accounts/login.html', {'form':'login'})

def signup(request):
    if request.method == 'POST':
        form = CreateNewCustomer(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CreateNewCustomer()
    return render(request, 'accounts/signup.html', {'form': form})

# class page request
class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home/index.html')

class About(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/about.html')


class Login(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'account/login.html')

class Logout(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'account/logout.html')

class Signup(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'account/signup.html')

class Menu(View):
	def get(self, request, *args, **kwargs):	
		starters = MenuItem.objects.filter(category__name__contains='Starters')
		mains = MenuItem.objects.filter(category__name__contains='Main')
		noodles = MenuItem.objects.filter(category__name__contains='Noodles')
		softdrinks = MenuItem.objects.filter(category__name__contains='SoftDrinks')
		wines = MenuItem.objects.filter(category__name__contains='Wine')
		desserts = MenuItem.objects.filter(category__name__contains='Desserts')
		vegetarian = MenuItem.objects.filter(category__name__contains='Vegetarian')
		# pass into context
		contect = {
			'starters': starters,
			'mains': mains,
			'noodles': noodles,
			'vegetarian': vegetarian,			
			'softdrinks': softdrinks,
			'wines': wines,
			'desserts': desserts,
		}
		return render(request, 'accounts/menu.html', contect)

class Contact(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/contact.html')

class Gallery(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'includes/gallery.html')

def updateItem(request):
	data = json.loads(request.body)
	menuid = data['menuid']
	action = data['action']
	print('Action:', action)
	print('MenuID:', menuid)

	customer = request.user.customer
	menu = MenuItem.objects.get(id=menuid)
	order, created = Order.objects.get_or_create(customer=customer, paymentStatus=False)
	orderDetail, created = OrderDetail.objects.get_or_create(order=order, menuItem_id=menuid)

	if action == 'add':
		orderDetail.quantity = (orderDetail.quantity + 1)
	elif action == 'remove':
		orderDetail.quantity = (orderDetail.quantity - 1)
	
	orderDetail.save()

	if orderDetail.quantity <= 0:
		orderDetail.delete()

	return JsonResponse('added to menu', safe=False)


class Cart(View):
	def get(self, request):	
		if request.user.is_authenticated:
			customer = request.user.customer
			order, created = Order.objects.get_or_create(customer=customer, paymentStatus=False)
			items = order.orderdetail_set.all()
			cartitems = order.get_cart_items
		
		else:
			#guest cart
			items = []
			order = {'get_cart_total':0, 'get_cart_items':0}
			cartitems = order['get_cart_items']

		context = {'items':items, 'order':order, 'cartitems':cartitems}
		return render(request, 'accounts/cart.html', context)


class checkout(View):
	def get(self, request):
		if request.user.is_authenticated:
			customer = request.user.customer
			order, created = Order.objects.get_or_create(customer=customer, paymentStatus=False)
			items = order.orderdetail_set.all()
			cartitems = order.get_cart_items
			
			name = Customer.objects.values_list('name', flat=True).get(id=customer.id)
			city = Customer.objects.values_list('city', flat=True).get(id=customer.id)
			postcode = Customer.objects.values_list('postcode', flat=True).get(id=customer.id)
			address = Customer.objects.values_list('homeAddress', flat=True).get(id=customer.id)
			phone = Customer.objects.values_list('phoneNumber', flat=True).get(id=customer.id)
			
		
		else:
			#guest cart
			items = []
			order = {'get_cart_total':0, 'get_cart_items':0}
			cartitems = order['get_cart_items']

		context = {'items':items, 'order':order, 'cartitems':cartitems, 'address':address, 'name':name, 'city':city, 'postcode':postcode, 'phone':phone}
		return render(request, 'accounts/checkout.html', context)
	
