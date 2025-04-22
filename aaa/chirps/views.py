# posts/views.py
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from itertools import chain
from datetime import datetime
from operator import attrgetter
from django.utils import timezone
from django.views import generic
from django.core import serializers
from django.core.serializers import serialize

from .models import Post
from .forms import PostForm, EditForm
from groups.models import Group, Comment
from blog.models import Blog
from shelf.models import Shelves

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()




# Shows lists of posts for user and/or group
@login_required
def list_post_create(request):
    form = PostForm(request.POST or None, request.FILES, user=request.user)
    post_list = Post.objects.all().order_by('-created_at')
    group = Group.objects.all()

    paginator = Paginator(post_list, 40) 
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.accepts('application/json'):
        if form.is_valid():
            form.instance.user = request.user
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Post added')

            return JsonResponse({
                'user': instance.user.username,
                'message': instance.message,
            })

    return render(request, 'chirps/posts.html', {'form': form, 'post_list': post_list, 'page_obj': page_obj})






# post detail
def post_detail(request, pk):
    item = Post.objects.get(pk=pk)
    form = PostForm()
    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'chirps/detail.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))




# post detail page
def post_detail_data(request, pk):
    obj = Post.objects.get(pk=pk)

    data = {
        'id': obj.id,
        'message': obj.message,
        #'group': obj.group,
        #'image': obj.image,
        'user': obj.user.username,
    }

    return JsonResponse({'data': data})





class SingleGroup(generic.DetailView):
	model = Group
	context_object_name = 'group_chirp'




#@login_required
def like_unlike_post(request):
    if request.accepts('application/json'):
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        pk = request.POST.get('pk')
        obj = Post.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked': liked, 'count': obj.like_count})




def edit_post(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(Post, pk=pk)
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.message = request.POST.get('message')
        #obj.group = request.POST.get('group')
        messages.success(request, 'Post Updated')
        obj.save(update_fields=['image', 'message'])

        context = {'obj': obj,}

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

    return render(request, 'chirps/modal_edit.html', context)


def delete_post(request, pk):
    if request.accepts('application/json'):
        # Attempt to retrieve and delete the object
        try:
            obj = Post.objects.get(pk=pk)
            obj.delete()
            # Construct the URL for the success page using reverse
            success_url = reverse("chirps:all")
            messages.success(request, 'Post Deleted')
            # Return a JSON response with the redirect URL
            return JsonResponse({'redirect_url': success_url})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Something went wrong'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
