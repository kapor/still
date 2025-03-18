from django.contrib import admin
from django.urls import include, path
from . import views
from .views import Create

app_name = 'groups'

urlpatterns = [
    path('', views.GroupView.as_view(), name='all'),

    path('grouplist', views.GroupView.as_view(), name='grouplist'),
    # path('new/', views.CreateGroup.as_view(), name='create'),
    # path('add/', views.AddGroup.as_view(), name='add'),
    path('', Create, name='create'),
    path('<slug>', views.SingleGroup, name='single'),
    path('<slug>/join', views.JoinGroup.as_view(), name='join'),
    path('<slug>/leave', views.LeaveGroup.as_view(), name='leave'),
    path('<slug>/delete', views.DeleteGroup.as_view(), name='delete'),

    # path('<slug>/comment', views.add_comment_to_group, name='comment'),
    path('comment/<int:pk>/delete/', views.CommentDelete, name='commentdelete'), 

    path('<slug>/new', views.GroupPost.as_view(), name='groupost'),

    path('formbutton', views.GroupPostFormButton.as_view(), name='formbutton'),

]

