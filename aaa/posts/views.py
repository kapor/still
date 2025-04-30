# posts/views.py
from . import models
from .models import Post
from . import forms
from posts.forms import PostForm, PostFormGroup, EditForm
from groups.models import Group
from django.db import transaction

from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import View, DetailView

from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()






# Shows lists of posts for user and/or group
@login_required
def list_post_create(request):
    form = PostForm(request.POST or None, request.FILES or None, user=request.user)
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
                # 'image': instance.image.url,
            })

    context = {'form': form, 'post_list': post_list, 'page_obj': page_obj}
    
    return render(request, 'posts/posts.html', context)




# def upload_multiple_files(request):
#     if request.method == 'POST':
#         form = MultipleFileInput(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_images = request.FILES.getlist('image')
#             for image in image:
#                 image.save()
#         return HttpResponse("Files uploaded successfully!")
#     else:
#         form = MultipleFileInput()





# post detail
def post_detail(request, pk):
    item = Post.objects.get(pk=pk)
    form = PostForm()
    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'posts/detail.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))




# post detail page
def post_detail_data(request, pk):
    obj = Post.objects.get(pk=pk)

    data = {
        'id': obj.id,
        'message': obj.message,
        'group': obj.group,
        'image': obj.image,
        'user': obj.user.username,
    }

    return JsonResponse({'data': data})









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







def delete_post(request, pk):
    if request.accepts('application/json'):
        # Attempt to retrieve and delete the object
        try:
            obj = Post.objects.get(pk=pk)
            obj.delete()
            # Construct the URL for the success page using reverse
            success_url = reverse("posts:all")
            messages.success(request, 'Post Deleted')
            # Return a JSON response with the redirect URL
            return JsonResponse({'redirect_url': success_url})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Something went wrong'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    





# def edit_post(request, pk):
#     obj = Post.objects.get(pk=pk)
#     form = EditForm()
#     group = Group.objects.all()

#     if request.accepts('application/json'):
#         new_message = request.POST.get('message')
#         new_group = request.POST.get('group')
#         new_image = request.POST.get('image')
#         obj.message = new_message
#         obj.group = new_group
#         obj.image = new_image
#         obj.save()

#     return JsonResponse({
#         'message': new_message,
#         'group': new_group,
#         'image': new_image,
#     })

@login_required
def edit_post(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(Post, pk=pk)
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.message = request.POST.get('message')
        # obj.group = request.POST.get('group')

        messages.success(request, 'Post Updated')
        obj.save(update_fields=['image', 'message'])

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)






class SingleGroup(generic.DetailView):
	model = Group
	context_object_name = 'group'






def post_detail_data(request, pk):
    obj = Post.objects.get(pk=pk)

    data = {
        'id': obj.id,
        'message': obj.message,
        'user': obj.user.username,
    }

    return JsonResponse({'data': data})





