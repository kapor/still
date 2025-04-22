from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from groups.models import Group, Comment
from blog.models import Blog
from shelf.models import Shelves
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
# from .forms import UserForm1, UserForm2
from . import forms

# Create your views here.



class SignUp(CreateView):
	form_class = forms.UserForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'





# Modal View
class Login(CreateView):
	template_name = 'accounts/login.html'
	fields = ('username', 'password')
	success_url = reverse_lazy('home')



# class reg():

#     def reg_join(request):

#         registered = False

#         user_form = UserForm1()
#         prof_form = UserForm2()

#         if request.method == 'POST':
#             user_form = forms.UserForm1(data=request.POST)
#             prof_form = forms.UserForm2(data=request.POST)

#             if user_form.is_valid() and prof_form.is_valid():

#                 user = user_form.save()
#                 user.set_password(user.password)
#                 user.save()

#                 profile = prof_form.save(commit=False)
#                 profile.user = user

#                 if 'picture' in request.FILES:
#                     profile.picture = request.FILES['photo']

#                 profile.save()

#                 registered = True
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('home'))
                
#             else:   
#                 print(user_form.errors, prof_form.errors)

#         else:
#             user_form = UserForm1()
#             prof_form = UserForm2()

#         return render(request, 'reg/join.html',{'user_form':user_form, 'prof_form':prof_form, 'registered':registered})



    # @login_required #decorator
    # def reg_loggedin(request):
    #     logout(request)
    #     return render(request, 'base/user.html', {})

    # @login_required #decorator
    # def reg_logout(request):
    #     logout(request)
    #     return render(request, 'accounts/login.html', {})





