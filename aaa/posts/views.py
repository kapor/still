# posts/views.py
from . import models
from . import forms
from posts.forms import PostForm, PostFormGroup
from groups.models import Group
from django.db import transaction

from django.http import Http404
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect

from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, RedirectView

from django.contrib.auth.decorators import login_required
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
        if form.is_valid():
            form.instance.user = request.user
        with transaction.atomic():
            post = form.save()
            return redirect('posts:all')
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







# Shows list view of specific user's posts
class UserPosts(generic.ListView, LoginRequiredMixin):
	model = models.Post
	template_name = 'posts/user_post_list.html'

	# upon calling 'UserPosts' it sets the current user's view to only see posts from the username of whoever is currently logged in
	def get_queryset(self):
		try:
			self.post_user = User.objects.prefetch_related("posts").get(username__iexact=self.kwargs.get("username"))
		except User.DoesNotExist:
			raise Http404
		else:
			return self.post_user.posts.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_user'] = self.post_user
		return context



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
	success_url = 'get_success_url'

	def get_success_url(self, *args, **kwargs):
		return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

	# def get_success_url(self, request):
	# 	return redirect(request.META['HTTP_REFERER'])


	# def get_success_url(self, request, *args, **kwargs):
	# 	referer = request.META.get('HTTP_REFERER')
	# 	if referer:
	# 		return HttpResponse(f"Referer: {referer}")
	# 	else:
	# 		return HttpResponse("No referer")


	# def get_success_url(self):
	# 	return HttpResponse('')
		# return redirect(request.META['HTTP_REFERER'])






def DeletePostConfirm(request, pk):
    post = models.Post.objects.filter(pk=pk)
    post.delete()
    return render(request, 'posts/post_confirm_delete.html', {'form': form})






# def ConfirmDelete(request):
#     previous_url = request.META.get('HTTP_REFERER')
#     request.session['previous_url'] = previous_url
#     return render(request, 'post_confirm_delete.html', {'previous_url': previous_url})


# class DeletePostGroup(DeleteView, LoginRequiredMixin, PrefetchRelatedMixin):
# 	model = models.Post
# 	prefetch_related = ('user', 'group')
# 	template_name = 'posts/post_confirm_delete.html'

# 	def post(self, request, group_slug, post_id):
# 		group = get_object_or_404(Group, slug=group_slug)
# 		post = get_object_or_404(Post, id=post_id, group=group)
# 		post.delete()
# 		return redirect('groups:single', slug=group_slug)











class SingleGroup(generic.DetailView):
	model = Group
	context_object_name = 'group'







def PostLoad(request):
    post_obj = models.Post.objects.all()[0:10]
    total_posts_obj = models.Post.objects.count()
    print(total_posts_obj)
    return render(request, 'posts/post_load.html', context={'posts': post_obj, 'total_posts_obj': total_posts_obj})






def PostMore(request):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 20
    post_obj = list(models.Post.objects.values()[offset_int:offset_int+limit])
    data = {
        'posts': post_obj
    }
    return JsonResponse(data=data)








