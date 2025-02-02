# aaa/groups/forms.html 
from . import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, RedirectView
from django.contrib import messages
from groups.models import Group, GroupMember
from groups.forms import GroupForm

from django_htmx.middleware import HtmxDetails
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# Create your views here.


class CreateGroup(LoginRequiredMixin, CreateView):
	fields = ('name', 'description')
	model = Group

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
    template_name = "groups/groups.html"
    context_object_name = "grouplist"
    paginate_by = 20
    ordering = "pk"
    # new method added ⬇️
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "groups/group_list.html"
        else:
            return self.template_name




class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails





