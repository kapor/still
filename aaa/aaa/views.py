# aaa/views.py
from __future__ import annotations

from django.views.generic import ListView, TemplateView, View
from posts.models import Post
from blog.models import Blog
from shelf.models import Shelves
from groups.models import Group, Comment

from django_htmx.middleware import HtmxDetails

from itertools import chain, groupby
from datetime import datetime
from operator import attrgetter
from django.utils import timezone
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import F

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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



class Activity(ListView):
    template_name = "index.html"
    ordering = "created_at"

    def get(self, request):
        post = Post.objects.all()
        comment = Comment.objects.all()
        blog = Blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        shelf = Shelves.objects.all()

        combined_list = list(chain(post, comment, blog, shelf))


        sorted_objects = sorted(
            combined_list,
            key=lambda obj: obj.created_at if hasattr(obj, 'created_at') else datetime('published_date'),
            reverse=True
        )
        
        # Paginate combined list
        paginator = Paginator(sorted_objects, 80)  # 10 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
        }

        return render(request, 'index.html', context)





    class SearchView(ListView):
        template_name = "index_search.html"
        context_object_name = 'results'
        ordering = "created_at"
        paginate_by = 100

        def get_queryset(self):

            query = self.request.GET.get('q')
            if query:
                return Shelves.objects.filter(
                    Q(year__icontains=query) | 
                    Q(title__icontains=query) | 
                    Q(author__icontains=query) | 
                    Q(publisher__icontains=query) | 
                    Q(description__icontains=query) | 
                    Q(notes__icontains=query)
                    )
            return Shelves.objects.all()



        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            page_obj = context['page_obj']
            context['query'] = self.request.GET.get('q', '')
            return context











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


































