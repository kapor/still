from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from shelf.models import Shelves
from . import models, forms
from shelf.forms import ShelfEntryForm, ShelfEntryEdit
from shelf import views, urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
import os



# Create your views here.


class ShelfListView(ListView):
	model = Shelves
	template_name = 'shelf/shelf_list.html'
	queryset = Shelves.objects.order_by('-id')
	paginate_by = 100
	# def get_queryset(self):
	# 	return super().get_queryset().filter(user=self.request.user)


class ShelfDetailView(DetailView):
    model = models.Shelves
    context_object_name = 'shelfdetail'
    template_name = 'shelf/shelf_detail.html'





# Modal View
@login_required
def ShelfAdd(request):
    form = forms.ShelfEntryForm()
    if request.method == 'POST':
        form = forms.ShelfEntryForm(request.POST, request.FILES)  
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            photo = form.save()
            form.save_m2m()
            return redirect('/shelf')
    else:
        form = forms.ShelfEntryForm()
    return render(request, 'shelf/shelf_modal.html',{'form':form})








class Edit_Item(LoginRequiredMixin, UpdateView):
    model = Shelves
    login_url = "login"
    template_name = 'shelf/shelf_form.html'
    redirect_field_name = 'shelf/shelf_detail.html'
    form_class = ShelfEntryEdit
    context_object_name = 'edit'




class Delete_Item(LoginRequiredMixin, DeleteView):
    model = Shelves
    template_name = 'shelf/shelf_confirm_delete.html'
    success_url = reverse_lazy("shelf:shelf")




