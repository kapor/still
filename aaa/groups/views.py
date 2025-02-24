# aaa/groups/forms.html 
from . import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib import messages
from groups.models import Group, GroupMember
from groups.forms import GroupForm
from django.http import Http404
from django.views import generic
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.



class SingleGroup(DetailView):
	model = Group

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



@login_required
def GroupPost(request, group_id):
	group = get_object_or_404(Group, pk=group_id)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.group = group
			post.save()
			return redirect('groups/group_detail.html', group_id=group_id)
	else:
		form = PostForm()
	posts = Post.objects.filter(group=group).order_by('-created_at')
	context = {'group': group, 'form': form, 'posts': posts}
	return render(request, 'groups/group_detail.html', context)




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









