# posts/views.py
from . import models
from .models import Post
from . import forms
from posts.forms import PostForm, PostFormGroup
from groups.models import Group, Comment
from blog.models import Blog
from shelf.models import Shelves
from django.db import transaction
from django.core.serializers import serialize

from django.utils import timezone
from django.http import Http404
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from itertools import chain
from datetime import datetime
from operator import attrgetter

from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, RedirectView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import PrefetchRelatedMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

from braces.views import SelectRelatedMixin

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()



# Modal View

# @login_required
# def AddPost(request):
#     if request.method != 'POST':
#         form = PostForm(user=request.user)	
#     else:
#         form = PostForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.instance.user = request.user
#             post = form.save(commit=False)
#             post.save()
#             photo = form.save()
#             messages.success(request, 'Post added')
#             return redirect('posts:all')
#     context = {'form':form}
#     return render(request, 'posts/post_modal.html', context)



# class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
# 	fields = ('message', 'group')
# 	model = models.Post
# 	template_name = 'posts/post_modal.html'
# 	success_url = reverse_lazy('posts:all')

# 	# Used to connect the post to the user 
# 	def form_valid(self, form):
# 		self.object = form.save(commit=False)
# 		self.object.user = self.request.user
# 		self.object.save
# 		return super().form_valid(form)




# Shows lists of posts for user and/or group
@login_required
def list_post_create(request):
    form = PostForm(request.POST, user=request.user)
    post_list = Post.objects.all().order_by('-created_at')
    group = Group.objects.all()

    if request.accepts('application/json'):
        if form.is_valid():
            instance = form.save(commit=False)
            form.instance.user = request.user
            instance.save()
            photo = form.save()
            messages.success(request, 'Post added')
            return JsonResponse({
                'user': instance.user.username,
                'message': instance.message,
                # 'group': instance.group,
            })

    context = {
        'form': form, 
        'post_list': post_list
    }


    return render(request, 'posts/posts.html', context)





## def load_post(request, num_posts):
# def load_post(request, **kwargs):
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         num_posts = kwargs.get('num_posts')
#         visible = 20
#         upper = num_posts
#         lower = upper - visible
#         size = Post.objects.all().count()
#         group = serializers.serialize('json', Group.objects.all())

#         qs = Post.objects.all().order_by('created_at')
#         # you cannot pass in a JSON response as a query set directly – so creating an empty dictionary and looping through an object and appending it to the dictionary is a solution.
#         data = []
#         for item in qs:
#             item = {
#                     'created_at': item.created_at,
#                     'message': item.message,
#                     'user': item.user.username,
#                     'group': item.group,
#                 }
#             data.append(item)

#         return JsonResponse({'data':data[lower:upper], 'size': size})










@login_required
def PostGroup(request):
    if request.method != 'POST':
        form = PostForm(user=request.user)	
    else:
        form = PostForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.instance.user = request.user
        with transaction.atomic():
            post = form.save()
            return redirect('groups:single', group_id=group_id)
            # return redirect('posts:group')
    return render(request, 'posts/post_form.html', {'form': form})







# Basic post detail view
# class PostDetail(PrefetchRelatedMixin, generic.DetailView, LoginRequiredMixin):
#     model = models.Post
#     prefetch_related = ('user', 'group')
#     template_name = 'posts/post_detail.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user__username__iexact = self.kwargs.get('username'))



# post detail form
def post_detail(request, pk):
    obj = Posts.objects.get(pk=pk)
    form = PostForm()
    context = {
        'obj': obj,
        'form': form,
    }
    return render(request, 'posts/detail.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))



class EditPost(LoginRequiredMixin, UpdateView):
	model = models.Post
	login_url = "login"






def delete_post(request, pk):
    if request.accepts('application/json'):
        # Attempt to retrieve and delete the object
        try:
            obj = Posts.objects.get(pk=pk)
            obj.delete()
            # Construct the URL for the success page using reverse
            success_url = reverse("posts:posts")
            # Return a JSON response with the redirect URL
            return JsonResponse({'redirect_url': success_url})
        except MyModel.DoesNotExist:
            return JsonResponse({'error': 'Something went wrong'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    




class SingleGroup(generic.DetailView):
	model = Group
	context_object_name = 'group'












