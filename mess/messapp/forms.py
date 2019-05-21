from django import forms
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm
from .models import *

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']

class MyForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    my_field = forms.DateField(widget=AdminDateWidget)
    

class RegForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'password', 'roll', 'subscribed_mess_hostel']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())