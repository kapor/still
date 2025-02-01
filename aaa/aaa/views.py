# aaa/views.py
from __future__ import annotations

from django.views.generic import ListView, TemplateView
from posts.models import Product
from groups.models import Group

from django_htmx.middleware import HtmxDetails
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render



class Home(TemplateView):
    template_name = "index.html"

class PostView(ListView):
    model = Group
    template_name = "index.html"
    context_object_name = "index_grid"
    paginate_by = 20
    ordering = "pk"
    # new method added ⬇️
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "index_grid.html"
        else:
            return self.template_name



class GroupView(ListView):
    model = Group
    template_name = "groups/group_list.html"
    context_object_name = "grouplist"
    paginate_by = 20
    ordering = "pk"
    # new method added ⬇️
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "groups/group_list2.html"
        else:
            return self.template_name


