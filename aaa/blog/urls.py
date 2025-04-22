from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from . import views
from posts import urls
from .views import ( 
    blog_list_create,
    like_unlike_blog,
    BlogDetailView,
    # BlogUpdateView,
    delete_post,
    edit_post,
    blog_publish,
    blog_detail_data,
)


app_name = 'blog'

urlpatterns = [


    path('', views.blog_list_create, name='blog_main'),
    path('like_unlike/', views.like_unlike_blog, name='like_unlike'),

    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update/', views.edit_post, name='edit'),
    path('<int:pk>/delete/', views.delete_post, name='delete'),
    path('<int:pk>/data/', views.blog_detail_data, name='blog_detail_data'),
    # path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='blog_edit'),



    # path('blog/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog_delete'),
    # path('blog/<int:pk>/delete/', views.BlogDeleteDraft.as_view(), name='blog_delete_draft'),
    
    # path('post/<int:pk>/comment/', views.add_comment_to_blog, name='add_comment_to_blog'),
    # path('blog/<int:pk>/approve/', views.comment_approve, name='comment_approve'), 
    # path('blog/<int:pk>/delete/', views.comment_remove, name='comment_remove'), 

    path('<int:pk>/publish/', views.blog_publish, name='blog_publish'), 

]


