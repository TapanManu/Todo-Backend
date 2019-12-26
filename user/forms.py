from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username=forms.CharField(label=("Username"),widget=forms.TextInput( attrs={'placeholder':
                                          ('Username'),
                                          'autofocus': 'autofocus','required':'true'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':('password')}))
	email = forms.EmailField(max_length=254)

	class Meta:
		model=User
		fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('website',)
