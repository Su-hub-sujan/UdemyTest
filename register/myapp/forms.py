from  django import forms
from django.contrib.auth.admin import User
from .models import ProfileInfo
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfile(forms.ModelForm):
    class Meta():
        model=ProfileInfo
        fields=('Portfolio_site','Profile_pic')