from . import models
from . import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Blog, Tags
from .forms import BlogForm, BlogUpdate
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView


# Create your views here.




class BlogListView(ListView):
	model = Blog
	template_name = 'blog/blog_list.html'
	def get_queryset(self):
		return Blog.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class BlogDetailView(DetailView):
	model = Blog
	context_object_name = 'blog_detail'
	template_name = 'blog/blog_detail.html'




class AddBlog(LoginRequiredMixin, CreateView):
	model = Blog
	login_url = "/login/"
	template_name = 'blog/blog_modal.html'
	form_class = BlogForm
	required = False
	success_url = reverse_lazy('blog:draft_list')




# @login_required
# def AddBlog(request):
#     form = BlogForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         images = request.FILES.getlist('image')  
#         for image in images:
#             image_ins = Image(image = image)
#             image_ins.save()
#         return redirect('blog_form2')
#     else:
#         form = forms.BlogForm()
#     return render(request, 'blog/blog_modal.html',{'form':form})





class BlogUpdateView(LoginRequiredMixin, UpdateView):
	model = Blog
	login_url = "login"
	template_name = 'blog/blog_form.html'
	form_class = BlogUpdate
	required = False


class BlogDelete(LoginRequiredMixin, DeleteView):
	model = Blog
	template_name = 'blog/blog_confirm_delete.html'
	redirect_field_name = 'blog/blog_detail.html'
	success_url = reverse_lazy('blog:blog_list')


class BlogDeleteDraft(LoginRequiredMixin, DeleteView):
	model = Blog
	template_name = 'blog/blog_confirm_delete.html'
	success_url = reverse_lazy('blog:blog_list')
	






class BlogDraftListView(LoginRequiredMixin, ListView):
	model = Blog
	login_url = "/login/"
	template_name = 'blog/draft_list.html'
	redirect_field_name = "blog/blog_list.html"
	# returning all posts that are null (isnull=true)
	def get_queryset(self):
		return Blog.objects.filter(published_date__isnull=True).order_by('create_date')



@login_required(login_url='login')
def blog_publish(request, pk):
	blog = get_object_or_404(Blog, pk=pk)
	blog.publish()
	return redirect('blog_detail', pk=pk)







#################################################
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


