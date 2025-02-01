# posts/views.py
from . import models
from . import forms
from groups.models import Group

from django.http import Http404
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import PrefetchRelatedMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from braces.views import SelectRelatedMixin

#importing get_user_model allows us to asign User to it
from django.contrib.auth import get_user_model
User = get_user_model()



# Shows lists of posts for user and/or group
class PostList(SelectRelatedMixin, generic.ListView):
	model = models.Post
	select_related = ('user', 'group')



# Shows list view of specific user's posts
class UserPosts(generic.ListView):
	model = models.Post
	template_name = 'posts/user_post_list.html'

	# upon calling 'UserPosts' it sets the current user's view to only see posts from the username of whoever is currently logged in
	def get_queryset(self):
		try:
			self.post_user = User.objects.prefetch_related('posts').get(username__iexact = self.kwargs.get('username'))
		except User.DoesNotExist:
			raise Http404
		else: 
			return self.post_user.posts.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['post_user'] = self.post_user
		return context



# Basic post detail view
class PostDetail(PrefetchRelatedMixin, generic.DetailView):
	model = models.Post
	prefetch_related = ('user', 'group')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user__username__iexact = self.kwargs.get('username'))




class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
	fields = ('message', 'group')
	model = models.Post

	# Used to connect the post to the user 
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)




class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
	model = models.Post
	select_related = ('user', 'group')
	success_url = reverse_lazy('posts:all')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(user_id = self.request.user.id)

	def delete(self, *args, **kwargs):
		messages.success(self.request, 'Post Deleted')
		return super().delete(*args, **kwargs)







