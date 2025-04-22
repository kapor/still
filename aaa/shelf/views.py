from django.shortcuts import render, redirect, get_object_or_404
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
from .forms import ShelfEntryForm, SearchForm, ShelfUpdateForm
from shelf import views, urls
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import os



# class SearchView(ListView):
#     model = Shelves
#     template_name = 'shelf/shelf_search_results.html'
#     context_object_name = 'results'
#     paginate_by = 100

#     def get_queryset(self):
#        query = self.request.GET.get('q')
#        if query:
#             return Shelves.objects.filter(
#                     Q(year__icontains=query) | 
#                     Q(title__icontains=query) | 
#                     Q(author__icontains=query) | 
#                     Q(publisher__icontains=query) | 
#                     Q(description__icontains=query) | 
#                     Q(notes__icontains=query)
#                 )
#        return Shelves.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         page_obj = context['page_obj']
#         context['query'] = self.request.GET.get('q', '')
#         return context



def shelf_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Shelves.objects.filter(
                Q(year__icontains=query) | 
                Q(title__icontains=query) | 
                Q(author__icontains=query) | 
                Q(publisher__icontains=query) | 
                Q(description__icontains=query) | 
                Q(notes__icontains=query)) 

    paginator = Paginator(results, 20) 
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page_number(paginator.num_pages)

    context = {'results': results, 'page_obj': page_obj, 'query': query}

    return render(request, 'shelf/shelf_search_results.html', context)






# Shows lists of posts for user and/or group
@login_required
def shelf_list_create(request):
    form = ShelfEntryForm(request.POST, request.FILES)
    shelf_list = Shelves.objects.all().order_by('-id')

    paginator = Paginator(shelf_list, 100) 
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.accepts('application/json'):
        if form.is_valid():
            form.instance.user = request.user
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()
            messages.success(request, 'item added')
            return JsonResponse({
                'title': instance.title,
                'author': instance.author,
                'year': instance.year,
                'tags': [tag.name for tag in instance.tags.all()],
                'description': instance.description,
                # 'image': instance.image,
            })


    context = {'form': form, 'page_obj': page_obj, 'shelf_list': shelf_list}

    return render(request, 'shelf/shelf.html', context)






def shelf_detail(request, pk):
    obj = Shelves.objects.get(pk=pk)
    form = ShelfUpdateForm()
    context = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'shelf/detail.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))



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
    }

    return JsonResponse({'data': data})



# Shows lists of posts for user and/or group
@login_required
def shelf_edit(request, pk):
    form = ShelfEntryForm(request.POST, request.FILES)
    if request.method == 'POST':
        obj = get_object_or_404(Shelves, pk=pk)
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.title = request.POST.get('title')
        obj.author = request.POST.get('author')
        obj.year = request.POST.get('year')
        obj.type = request.POST.get('type')
        obj.publisher = request.POST.get('publisher')
        obj.artist = request.POST.get('artist')
        obj.quality = request.POST.get('quality')
        obj.price = request.POST.get('price')
        obj.location = request.POST.get('location')
        obj.tags = request.POST.get('tags')
        obj.weight = request.POST.get('weight')
        obj.pages = request.POST.get('pages')
        obj.isbn = request.POST.get('isbn')
        obj.description = request.POST.get('description')
        obj.notes = request.POST.get('notes')

        obj.save()

        messages.success(request, 'Post Updated')


        

        # obj.save(update_fields=['title', 'author', 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'weight', 'pages', 'isbn', 'description', 'notes', 'image'])

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)




# class Edit_Item(LoginRequiredMixin, UpdateView):
#     model = Shelves
#     login_url = "login"
#     template_name = 'shelf/shelf_form.html'
#     redirect_field_name = 'shelf/detail.html'
#     form_class = ShelfEntryForm
#     context_object_name = 'edit'



@login_required(login_url='login')
def shelf_delete(request, pk):
    if request.accepts('application/json'):
        # Attempt to retrieve and delete the object
        try:
            obj = Shelves.objects.get(pk=pk)
            obj.delete()
            # Construct the URL for the success page using reverse
            success_url = reverse("shelf:shelf")
            messages.success(request, 'Item Deleted')
            # Return a JSON response with the redirect URL
            return JsonResponse({'redirect_url': success_url})
        except Shelves.DoesNotExist:
            return JsonResponse({'error': 'Something went wrong'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



#@login_required
def like_unlike_shelf(request):
    if request.accepts('application/json'):
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        pk = request.POST.get('pk')
        obj = Shelves.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked': liked, 'count': obj.like_count})




# class Delete_Item(LoginRequiredMixin, DeleteView):
#     model = Shelves
#     template_name = 'shelf/shelf_confirm_delete.html'
#     success_url = reverse_lazy("shelf:shelf")




