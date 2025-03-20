from django.contrib import admin
from django.urls import include, path
from . import views
from groups import urls

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='all'),

    path('by/<username>/<pk>', views.PostDetail.as_view(), name='single'),
    path('delete/<pk>', views.DeletePost.as_view(), name='delete'),

    path('edit/<pk>', views.EditPost.as_view(), name='edit'),
    path('posts/in/<slug>', views.SingleGroup.as_view(), name='group'),

    path('new/', views.CreatePost.as_view(), name='create'),
    path('add/', views.AddPost, name='add'),

    path('postadd/', views.PostGroup, name='postgroup'),


]
