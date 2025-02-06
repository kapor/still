from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from . import forms
# Create your views here.



class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'


# Modal View
class Login(CreateView):
	template_name = 'accounts/login.html'
	fields = ('username', 'password')
	success_url = reverse_lazy('home')



