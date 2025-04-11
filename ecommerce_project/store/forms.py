from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import *

USER_ROLES = (
    ('customer', 'Customer'),
    ('seller', 'Seller'),
    ('admin', 'Admin'),
)
class CustomerForm(ModelForm):
    class Meta: 
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' #creates a form with all the fields from Order class

class CreateUserForm(UserCreationForm):
    role = forms.ChoiceField(choices = USER_ROLES) 
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','role', 'username', 'email', 'password1', 'password2']