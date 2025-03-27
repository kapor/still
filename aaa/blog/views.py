from . import models
from . import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from .models import Blog, Tags
from .forms import BlogForm, BlogUpdate
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages 
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()



class BlogListView(ListView):
	model = Blog
	template_name = 'blog/blog.html'
	paginate_by = 4

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = forms.BlogForm(self.request.POST, self.request.FILES)
		context['Published'] = Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
		context['Drafts'] = Blog.objects.filter(published_date__isnull=True).order_by('-created_at')

		return context


	def post(self, request, *args, **kwargs):
		form = forms.BlogForm(self.request.POST, self.request.FILES)

		if request.accepts('application/json'):
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				photo = form.save()
				form.save_m2m()
				return JsonResponse({
					'title': instance.title,
					'message': instance.message,
	                # 'image': instance.image,
				})

		return render(request, 'blog/blog.html', {'form': form })



def blog_main(request):
	view = BlogListView.as_view()
	return view(request)




# @login_required
# def add_blog(request):
# 	form = BlogForm(request.POST)

# 	if request.accepts('application/json'):
# 		form = forms.BlogForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			instance = form.save(commit=False)
# 			instance.save()
# 			photo = form.save()
# 			form.save_m2m()
# 			return JsonResponse({
# 				'title': instance.title,
# 				'message': instance.message,
# 				'created_at': instance.created_at,
#                 'image': instance.image,
# 			})
# 	return render(request, 'blog/blog.html', {'form': form })




# class BlogPublishListView(LoginRequiredMixin, ListView):
# 	model = Blog
# 	login_url = "/login/"
# 	template_name = 'blog/published.html'
# 	# returning all posts that are null (isnull=true)
# 	def get_queryset(self):
# 		return Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


# class BlogDraftListView(LoginRequiredMixin, ListView):
# 	model = Blog
# 	login_url = "/login/"
# 	template_name = 'blog/drafts.html'
# 	# returning all posts that are null (isnull=true)
# 	def get_queryset(self):
# 		return Blog.objects.filter(published_date__isnull=True).order_by('-created_at')









class BlogDetailView(DetailView):
	model = Blog
	context_object_name = 'blog_detail'
	template_name = 'blog/blog_detail.html'


# class AddBlog(LoginRequiredMixin, CreateView):
# 	model = Blog
# 	login_url = "/login/"
# 	template_name = 'blog/modal.html'
# 	form_class = BlogForm
# 	required = False

# 	def post(self, request, *args, **kwargs):
# 		messages.success(self.request, "Post successfully added")
# 		return super().post(request, *args, **kwargs)






class BlogUpdateView(LoginRequiredMixin, UpdateView):
	model = Blog
	login_url = "login"
	template_name = 'blog/blog_form.html'
	form_class = BlogUpdate
	required = False

	def post(self, request, *args, **kwargs):
		messages.success(self.request, "Post successfully updated")
		return super().post(request, *args, **kwargs)


class BlogDelete(LoginRequiredMixin, DeleteView):
	model = Blog
	template_name = 'blog/blog_confirm_delete.html'
	redirect_field_name = 'blog/blog_detail.html'
	success_url = reverse_lazy('blog:blog_list')

	def post(self, request, *args, **kwargs):
		messages.success(self.request, "Post successfully deleted")
		return super().post(request, *args, **kwargs)


class BlogDeleteDraft(LoginRequiredMixin, DeleteView):
	model = Blog
	template_name = 'blog/blog_confirm_delete.html'
	success_url = reverse_lazy('blog:blog_list')
	

	def post(self, request, *args, **kwargs):
		messages.success(self.request, "Post successfully deleted")
		return super().post(request, *args, **kwargs)




@login_required(login_url='login')
def blog_publish(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	blog.publish()
	return redirect('blog_detail', pk=pk)

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



class AddBlog(LoginRequiredMixin, CreateView):
	model = Blog
	login_url = "/login/"
	template_name = 'blog/drafts.html'
	form_class = BlogForm
	required = False

	def add_blog(request):
		form = BlogForm(request.POST)

		if request.accepts('application/json'):
			form = forms.BlogForm(request.POST, request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				photo = form.save()
				form.save_m2m()
				messages.success(request, 'Post added')
				return JsonResponse({
					'title': instance.title,
					'message': instance.message,
					'created_at': instance.created_at,
	                'image': instance.image,
				})

		return render(request, {'form': form, 'blog_list': blog_list})

		def post(self, request, *args, **kwargs):
			messages.success(self.request, "Post successfully added")
			return super().post(request, *args, **kwargs)





# COMMENTS
#################################################



@login_required(login_url='login')
def add_comment_to_blog(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	if request.method == 'POST':
		form = BlogCommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.blog = blog
			comment.save()
			return redirect('blog_detail', pk=blog.pk)
	else:
		form = BlogCommentForm()
	return render(request, 'blog/comment_form.html',{'form':form})




@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog_detail', pk=comment.blog.pk)



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    # Check if the user is authorized to delete the comment
    if request.user == comment.author or request.user.is_staff:
        comment.delete()

    return redirect('blog_detail', pk=comment.blog.pk)  # Redirect to the blog


