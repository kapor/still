from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/new/', views.BlogCreateView.as_view(), name='new'),

    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/remove/', views.BlogDeleteView.as_view(), name='blog_remove'),
    path('drafts/', views.BlogDraftListView.as_view(), name='draft_list'),
    path('blog/<int:pk>/approve/', views.comment_approve, name='comment_approve'), 
    path('blog/<int:pk>/delete/', views.comment_remove, name='comment_remove'), 
    path('blog/<int:pk>/publish/', views.blog_publish, name='blog_publish'), 

]


