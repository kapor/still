from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from . import views
from posts import urls




urlpatterns = [

    path('', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),

    path('blog/new/', views.AddBlog.as_view(), name='add'),
    # path('blog/new/', views.AddBlog, name='add'), 

    path('blog/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog_delete'),
    
    path('drafts/', views.BlogDraftListView.as_view(), name='draft_list'),
    path('blog/<int:pk>/delete/', views.BlogDeleteDraft.as_view(), name='blog_delete_draft'),
    
    path('post/<int:pk>/comment/', views.add_comment_to_blog, name='add_comment_to_blog'),
    path('blog/<int:pk>/approve/', views.comment_approve, name='comment_approve'), 
    path('blog/<int:pk>/delete/', views.comment_remove, name='comment_remove'), 

    path('blog/<int:pk>/publish/', views.blog_publish, name='blog_publish'), 

]


