from django import forms
form django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfo(forms.ModelForm):
    class Meta():
        fields = ('portfolio_site','profile_pic')        
