from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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