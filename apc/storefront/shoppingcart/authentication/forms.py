from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
import logging
from ..authentication.models import Customer, OrderDetail

log = logging.getLogger(__name__)

class CreateNewCustomer(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone_number = forms.IntegerField()
    home_address = forms.CharField(max_length=254)
    city = forms.CharField(max_length=30)
    postcode = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','phone_number','home_address','city','postcode', 'email', 'password1', 'password2', )
        
        
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    def signup(self, request, user):
        customer = Customer()
        phone_number = request.POST.get('phonenumber')
        home_address = request.POST.get('homeaddress')
        city = request.POST.get('city')
        post_code = request.POST.get('postcode')
        
        customer.user = user.first_name
        customer.phoneNumber = phone_number
        customer.city = city
        customer.postcode = post_code
        customer.homeAddress = home_address
        customer.createDate = datetime.today()
        log.info( phone_number  + " : " + home_address + " : "  + customer)
        customer.save(self)
        
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        log.info( user.first_name  + " : " + user.last_name)
        print( user.first_name  + " : " + user.last_name)
        # Add your own processing here.

        # You must return the original result.
        return user
        
        
        
        
        
    