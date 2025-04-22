from . import models
from . import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from .models import Blog, Tags
from .forms import BlogForm, BlogUpdate
from itertools import chain, groupby
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages 
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()



@login_required
def blog_list_create(request):
	form = BlogForm(request.POST or None, request.FILES or None)

	published = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	drafts = Blog.objects.filter(published_date__isnull=True).order_by('-created_at')


	combined_list = list(chain(published, drafts))

	sorted_objects = sorted(
		combined_list,
		key=lambda obj: obj.created_at if hasattr(obj, 'created_at') else datetime('published_date'),
		reverse=True
	)


	paginator = Paginator(published, 20) 
	page_number = request.GET.get('page', 1)
	page_obj = paginator.get_page(page_number)


	if request.accepts('application/json'):
		if form.is_valid():
			form.instance.user = request.user
			instance = form.save(commit=False)
			instance.save()
			form.save_m2m()
			messages.success(request, 'Item posted to drafts')
			return JsonResponse({
					'title': instance.title,
					'message': instance.message,
					'tags': [tag.name for tag in instance.tags.all()],
					# 'image': instance.image,
				})

	context = {'form': form, 'page_obj': page_obj, 'published': published, 'drafts': drafts, 'sorted_objects': sorted_objects}

	return render(request, 'blog/blog.html', context)



def blog_main(request):
	view = BlogListView.as_view()
	return view(request)



# post detail
def blog_detail(request, pk):
    item = Blog.objects.get(pk=pk)
    form = BlogUpdate()
    context = {
        'item': item,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))




# post detail page
def blog_detail_data(request, pk):
    obj = Blog.objects.get(pk=pk)

    data = {
        'id': obj.id,
        'title': obj.title,
        'message': obj.message,
        # 'group': obj.group,
        # 'tags': obj.tags,
        # 'image': obj.image,
        'user': obj.user.username,
    }

    return JsonResponse({'data': data})







@login_required
def like_unlike_blog(request):
    if request.accepts('application/json'):
    #if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        pk = request.POST.get('pk')
        obj = Blog.objects.get(pk=pk)
        if request.user in obj.liked.all():
            liked = False
            obj.liked.remove(request.user)
        else:
            liked = True
            obj.liked.add(request.user)
        return JsonResponse({'liked': liked, 'count': obj.like_count})





class BlogDetailView(DetailView):
	model = Blog
	context_object_name = 'blog_detail'
	template_name = 'blog/detail.html'



# class BlogUpdateView(LoginRequiredMixin, UpdateView):
# 	model = Blog
# 	login_url = "login"
# 	template_name = 'blog/blog_modal_edit.html'
# 	form_class = Blog
# 	required = False

# 	def post(self, request, *args, **kwargs):
# 		messages.success(self.request, "Post updated")
# 		return super().post(request, *args, **kwargs)



def edit_post(request, pk):
	if request.method == 'POST' and request.accepts('application/json'):
		obj = get_object_or_404(Blog, pk=pk)
		if 'image' in request.FILES:
			obj.image = request.FILES['image']

		obj.title = request.POST.get('title')
		obj.message = request.POST.get('message')
		obj.tags = request.POST.get('tags')

		messages.success(request, 'Post Updated')
		obj.save(update_fields=['image', 'title', 'message'])



		return redirect('blog:blog_detail', pk=pk)
	else:
		return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)







class BlogDeleteDraft(LoginRequiredMixin, DeleteView):
	model = Blog
	template_name = 'blog/blog_confirm_delete.html'
	success_url = reverse_lazy('blog:blog_list')
	

	def post(self, request, *args, **kwargs):
		messages.success(self.request, "Post successfully deleted")
		return super().post(request, *args, **kwargs)


@login_required(login_url='login')
def delete_post(request, pk):
    if request.accepts('application/json'):
        # Attempt to retrieve and delete the object
        try:
            obj = Blog.objects.get(pk=pk)
            obj.delete()
            # Construct the URL for the success page using reverse
            success_url = reverse("posts:all")
            messages.success(request, 'Post Deleted')
            # Return a JSON response with the redirect URL
            return JsonResponse({'redirect_url': success_url})
        except Blog.DoesNotExist:
            return JsonResponse({'error': 'Something went wrong'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@login_required(login_url='login')
def blog_publish(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	blog.publish()
	return redirect('blog:blog_detail', pk=pk)

	def post(self, request, *args, **kwargs):
		messages.success(self.request, "Post is now published")
		return super().post(request, *args, **kwargs)






#################################################
#################################################
#################################################
#################################################
# NOT IN USE
#################################################
#################################################
#################################################
#################################################





# @login_required
# def list_blog_create(request):
# 	form = BlogForm(request.POST)
# 	blog_list = Blog.objects.all().order_by('-created_at')

# 	if request.accepts('application/json'):
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			instance.save()
# 			photo = form.save()
# 			form.save_m2m()
# 			messages.success(request, 'Post added')
# 			return JsonResponse({
# 				'title': instance.title,
# 				'message': instance.message,
# 				'created_at': instance.created_at,
# 				'image': instance.image
# 			})

# 	return render(request, 'blog/blog.html', {'form': form, 'blog_list': blog_list})


# 	def post(self, request, *args, **kwargs):
# 		messages.success(self.request, "Post successfully added")
# 		return super().post(request, *args, **kwargs)



# class AddBlog(LoginRequiredMixin, CreateView):
# 	model = Blog
# 	login_url = "/login/"
# 	template_name = 'blog/drafts.html'
# 	form_class = BlogForm
# 	required = False

# 	def add_blog(request):
# 		form = BlogForm(request.POST)

# 		if request.accepts('application/json'):
# 			form = forms.BlogForm(request.POST, request.FILES, user=request.user)
# 			if form.is_valid():
# 				instance = form.save(commit=False)
# 				instance.user = request.user
# 				instance.save()
# 				photo = form.save()
# 				form.save_m2m()
# 				messages.success(request, 'Post added')
# 				return JsonResponse({
# 					'title': instance.title,
# 					'message': instance.message,
# 					'created_at': instance.created_at,
# 	                'image': instance.image,
# 				})

# 		return render(request, {'form': form, 'blog_list': blog_list})

# 		def post(self, request, *args, **kwargs):
# 			messages.success(self.request, "Post successfully added")
# 			return super().post(request, *args, **kwargs)





# COMMENTS
#################################################



# @login_required(login_url='login')
# def add_comment_to_blog(request, pk):
# 	blog = get_object_or_404(Blog, pk=pk)
# 	if request.method == 'POST':
# 		form = BlogCommentForm(request.POST)
# 		if form.is_valid():
# 			comment = form.save(commit=False)
# 			comment.blog = blog
# 			comment.save()
# 			return redirect('blog_detail', pk=blog.pk)
# 	else:
# 		form = BlogCommentForm()
# 	return render(request, 'blog/comment_form.html',{'form':form})




# @login_required
# def comment_approve(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)
#     comment.approve()
#     return redirect('blog_detail', pk=comment.blog.pk)



# @login_required
# def comment_remove(request, pk):
#     comment = get_object_or_404(Comment, pk=pk)

#     # Check if the user is authorized to delete the comment
#     if request.user == comment.author or request.user.is_staff:
#         comment.delete()

#     return redirect('blog_detail', pk=comment.blog.pk)  # Redirect to the blog


