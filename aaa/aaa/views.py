# aaa/views.py
from __future__ import annotations

from django.views.generic import ListView, TemplateView
from posts.models import Post
from groups.models import Group

from django_htmx.middleware import HtmxDetails
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers



class Home(TemplateView):
    template_name = "index.html"

# class PostView(ListView):
#     model = Post
#     template_name = "posts/post_grid.html"
#     context_object_name = "post_grid"
#     paginate_by = 20
#     ordering = "pk"
#     # new method added ⬇️
#     def get_template_names(self, *args, **kwargs):
#         if self.request.htmx:
#             return "posts/post_list.html"
#         else:
#             return self.template_name



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





def IndexLoad(request):
    group_obj = Group.objects.all()[0:10]
    total_obj = Group.objects.count()
    print(total_obj)
    return render(request, 'index_load.html', context={'groups': group_obj, 'total_obj': total_obj})


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


































