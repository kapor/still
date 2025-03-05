# aaa/groups/forms.html 
from . import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib import messages
from groups.models import Group, GroupMember, Comment
from groups.forms import GroupForm, CommentForm
from posts.forms import PostFormGroup, PostForm
from posts.models import Post
from django.http import Http404
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.forms.models import inlineformset_factory
from django.forms import modelformset_factory




GroupFormset = modelformset_factory(Post, fields=('message',),)


# class SingleGroup(LoginRequiredMixin, DetailView):
# 	model = Group




@login_required
def SingleGroup(request, slug):
	group = get_object_or_404(Group, slug=slug)
	comment = Comment.objects.filter(group=group)
	post = Post.objects.filter(group=group)
	context = {}
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.group = group
			comment.user = request.user
			comment.save()
			return redirect('groups:single', slug=slug)
	else:
		form = CommentForm()
		context = {'comment': comment, 'group': group, 'form': form}
	return render(request, 'groups/group_detail.html', context)









def CommentDelete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    group_slug = comment.group.slug  # Retrieve the post's slug
    comment.delete()
    return redirect(reverse('groups:single', kwargs={'slug': group_slug}))






class ListGroups(ListView):
	model = Group
	context_object_name = "groups"



class JoinGroup(LoginRequiredMixin, RedirectView):
	
	def get_redirect_url(self, *args, **kwargs):
		return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):
		group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
		try:
			GroupMember.objects.create(user = self.request.user, group=group)
		except IntegrityError:
			messages.warning(self.request, ('Already a member.'))
		else:
			messages.success(self.request, ("You're now a member."))
		return super().get(request, *args, **kwargs)



class LeaveGroup(LoginRequiredMixin, RedirectView):
	
	def get_redirect_url(self, *args, **kwargs):
		return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):
		try:
			membership = models.GroupMember.objects.filter(
				user=self.request.user,
				group__slug=self.kwargs.get('slug')
			).get()
		except models.GroupMember.DoesNotExist:
			messages.warning(self.request, "You are not in this group")
		else: 
			membership.delete()
			messages.success(self.request, 'You have left the group')
		return super().get(request, *args, **kwargs)




class GroupView(ListView):
    model = Group
    fields = ('name', 'description', 'members')
    template_name = "groups/_groups.html"
    context_object_name = "grouplist"
    paginate_by = 20
    # ordering = 'pk'
    ordering = ['name']
    # new method added ⬇️
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "groups/group_list.html"
        else:
            return self.template_name





class GroupPost(LoginRequiredMixin, RedirectView):
	fields = ('message', 'group')
	model = Post
	template_name = 'group_detail_post.html'

	def get_redirect_url(self, *args, **kwargs):
		return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

	def get(self, request, *args, **kwargs):
		group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
		return super().get(request, *args, **kwargs)

	def get_form(self, form_class=None):
		return GroupFormset(**self.get_form_kwargs(), instance=self.object)






class CreateGroup(LoginRequiredMixin, CreateView):
	model = Group
	form_class = GroupForm
  



# Modal View
class AddGroup(LoginRequiredMixin,generic.CreateView,):
	template_name = 'groups/group_modal.html'
	model = models.Group
	context_object_name = 'addgroup'
	form_class = GroupForm





class DeleteGroup(LoginRequiredMixin, generic.DeleteView):
	model = models.Group
	context_object_name = 'deletegroup'
	success_url = reverse_lazy('groups:all')

	def delete(self, *args, **kwargs):
		messages.success(self.request, 'Group Deleted')
		return super().delete(*args, **kwargs)




class GroupPostFormButton(DetailView):
	template_name = "groups/group_post_form_button.html"


















