from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from shelf.models import ShelfList
from shelf import views, urls
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from . import models
import os

# Create your views here.


class ShelfListView(ListView):
	model = models.ShelfList
	paginate_by = 20
	queryset = ShelfList.objects.order_by('-id')
	#Below filters items only created by the logged-in user
	def get_queryset(self):
		return super().get_queryset().filter(user=self.request.user)

