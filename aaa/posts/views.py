# posts/views.py
from . import models
from . import forms
from posts.forms import PostForm, PostFormGroup
from groups.models import Group, Comment
from blog.models import Blog
from shelf.models import Shelves
from django.db import transaction

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
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import PrefetchRelatedMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

from braces.views import SelectRelatedMixin

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()



# Modal View

@login_required
def AddPost(request):
    if request.method != 'POST':
        form = PostForm(user=request.user)	
    else:
        form = PostForm(data=request.POST, user=request.user)
        # if form.is_valid():
        #     form.instance.user = request.user
        if form.is_valid():
            form.instance.user = request.user
            post = form.save(commit=False)
            post.save()
            photo = form.save()
            messages.success(request, 'Post added')
            return redirect('posts:all')
        # with transaction.atomic():
        #     post = form.save()
        #     photo = form.save()
        #     messages.success(request, 'Post added')
        #     return redirect('posts:all')
    context = {'form':form}
    return render(request, 'posts/post_modal.html', context)





class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	fields = ('message', 'group')
	model = models.Post
	template_name = 'posts/post_modal.html'
	success_url = reverse_lazy('posts:all')

	# Used to connect the post to the user 
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save
		return super().form_valid(form)





	
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




















# Shows lists of posts for user and/or group
class PostList(LoginRequiredMixin, PrefetchRelatedMixin, generic.ListView):
	model = models.Post
	template_name = 'posts/post_list.html'
	prefetch_related = ('user', 'group')










# Basic post detail view
class PostDetail(PrefetchRelatedMixin, generic.DetailView, LoginRequiredMixin):
	model = models.Post
	prefetch_related = ('user', 'group')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user__username__iexact = self.kwargs.get('username'))


class EditPost(LoginRequiredMixin, UpdateView):
	model = models.Post
	login_url = "login"




class DeletePost(LoginRequiredMixin, PrefetchRelatedMixin, generic.DeleteView):
    model = models.Post
    prefetch_related = ('user', 'group')
    template_name = 'posts/post_confirm_delete.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Post removed")
        return super().post(request, *args, **kwargs)













class SingleGroup(generic.DetailView):
	model = Group
	context_object_name = 'group'













