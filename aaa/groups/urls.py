from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupView.as_view(), name='all'),

    path('grouplist', views.GroupView.as_view(), name='grouplist'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<slug>', views.SingleGroup.as_view(), name='single'),
    path('join/<slug>', views.JoinGroup.as_view(), name='join'),
    path('leave/<slug>', views.LeaveGroup.as_view(), name='leave'),
    path('add/', views.AddGroup.as_view(), name='add'),
    path('delete/<slug>', views.DeleteGroup.as_view(), name='delete'),
]

