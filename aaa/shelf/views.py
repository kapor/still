from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse, reverse_lazy
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from shelf.models import Shelves
from accounts.models import UserInfo
from django.db.models import Q
from . import models, forms
from .forms import ShelfEntryForm, ShelfEntryEdit, SearchForm
from shelf import views, urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import os









class SearchView(ListView):
    model = Shelves
    template_name = 'shelf/shelf_search_results.html'
    context_object_name = 'results'
    paginate_by = 100

    def get_queryset(self):
       query = self.request.GET.get('q')
       if query:
            return Shelves.objects.filter(
                    Q(year__icontains=query) | 
                    Q(title__icontains=query) | 
                    Q(author__icontains=query) | 
                    Q(publisher__icontains=query) | 
                    Q(description__icontains=query) | 
                    Q(notes__icontains=query)
                )
       return Shelves.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_obj = context['page_obj']
        context['query'] = self.request.GET.get('q', '')
        return context






def create_post(request):
    form = PostForm(request.POST or None)
    qs = Posts.objects.all()

    if request.accepts('application/json'):
        if form.is_valid():
            author = Profile.objects.get(user=request.user)
            instance = form.save(commit=False)
            instance.author = author
            instance.save()
            return JsonResponse({
                'title': instance.title,
                'message': instance.message,
                'author': instance.author.user.username,
                'id': instance.id
            })

    return render(request, 'main.html', {'form': form})



@login_required
def shelf_list_create(request):
    form = ShelfEntryForm(request.POST or None)
    shelf_list = Shelves.objects.order_by('-id')
    paginator = Paginator(shelf_list, 100) 
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.accepts('application/json'):
        if form.is_valid():
            instance = form.save(commit=False)
            form.instance.user = request.user
            photo = form.save()
            messages.success(request, 'New item added')
            instance.save()
            return JsonResponse({
                'title': instance.title,
                'author': instance.author,
                'year': instance.year,
                'type': instance.type,
                'publisher': instance.publisher,
                'artist': instance.artist,
                'quality': instance.quality,
                'price': instance.price,
                'location': instance.location,
                'genre': instance.genre,
                # 'tags': instance.tags,
                'weight': instance.weight,
                'pages': instance.pages,
                'isbn': instance.isbn,
                'description': instance.description,
                'notes': instance.notes,
                # 'image': instance.image,
            })

    context = {'form': form, 'page_obj': page_obj}

    return render(request, 'shelf/shelf.html', context)



def shelf_detail_view(request, pk):
    obj = Shelves.objects.get(pk=pk)
    form = ShelfEntryForm()
    context = {'obj': obj, 'form': form} 

    return render(request, 'shelf/shelf_detail.html', context)


def shelf_detail_data(request, pk):
    obj = Shelves.objects.get(pk=pk)
    data = {
        'id': obj.id,
        'title': obj.title,
        'author': obj.author,
        'year': obj.year,
        'type': obj.type,
        'publisher': obj.publisher,
        'artist': obj.artist,
        'quality': obj.quality,
        'price': obj.price,
        'location': obj.location,
        'genre': obj.genre,
        # 'tags': obj.tags,
        'weight': obj.weight,
        'pages': obj.pages,
        'isbn': obj.isbn,
        'description': obj.description,
        'notes': obj.notes,
        # 'image': obj.image,

        #another way to add permissions is to compare the "user" who authored the item and the user who's currently "logged_in"
        'user': obj.user.username,
        'logged_in': request.user.username
    }

    return JsonResponse({'data': data})



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




