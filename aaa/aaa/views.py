# aaa/views.py
from __future__ import annotations

from django.views.generic import ListView, TemplateView
from posts.models import Post
from groups.models import Group, Comment

from django_htmx.middleware import HtmxDetails
from itertools import chain
from datetime import datetime
from operator import attrgetter
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.core import serializers



class Home(TemplateView):
    template_name = "index.html"

class IndexView(ListView):
    model = Group
    template_name = "index.html"
    context_object_name = "index_grid"
    paginate_by = 20
    ordering = "name"
    # new method added ⬇️

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "index_grid.html"
        else:
            return self.template_name




def Activity(request):
    post = Post.objects.all()
    comment = Comment.objects.all()

    combined_list = list(chain(post, comment))

    sorted_objects = sorted(
        combined_list,
        key=lambda obj: obj.created_at if hasattr(obj, 'created_at') else datetime(1970, 1, 1),
        reverse=True
    )
    
    context = {
        'data': sorted_objects,
    }
    return render(request, 'index.html', context)







def IndexLoad(request):
    group_obj = Group.objects.all()[0:10]
    total_obj = Group.objects.count()
    context={
        'groups': group_obj, 
        'total_obj': total_obj
    }
    print(total_obj)

    return render(request, 'index_load.html', context)


def load_more(request):
    offset = request.GET.get('offset')
    offset_int = int(offset)
    limit = 20
    # group_obj = group.objects.all()[offset_int:offset_int+limit]
    group_obj = list(Group.objects.values()[offset_int:offset_int+limit])
    data = {
        'groups': group_obj
    }
    return JsonResponse(data=data)


































