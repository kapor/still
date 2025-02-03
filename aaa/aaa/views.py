# aaa/views.py
from __future__ import annotations
import json

from posts.models import Product, Post
from groups.models import Group

from django.views.generic import ListView, TemplateView
from django_htmx.middleware import HtmxDetails
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404





class Home(TemplateView):
    template_name = "index.html"

class PostView(ListView):
    model = Post
    template_name = "posts/post_grid.html"
    context_object_name = "post_grid"
    paginate_by = 20
    ordering = "pk"
    # new method added ⬇️
    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "posts/post_list.html"
        else:
            return self.template_name


class IndexView(ListView):
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



