from django import forms
from django.forms import ModelForm 
from accounts.models import UserInfo
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):

	class Meta: 
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()

	#another way to add labels to the fields
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].label = 'Username'
		self.fields['email'].label = 'Email'



class UserForm2(forms.ModelForm):

	class Meta():
		model = UserInfo
		fields = ('picture',)



