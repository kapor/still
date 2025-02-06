"""
URL configuration for aaa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from .views import IndexLoad, load_more



urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace="posts")),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('groups/', include('groups.urls', namespace='groups')),
    path("", views.IndexView.as_view(template_name='index.html'), name="home"),

    path('index_load/', IndexLoad, name='index_load'),
    path('load/', load_more, name='load'),


]


