from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import include, path
from . import views
from groups import urls

app_name = 'posts'

urlpatterns = [
    path('', views.list_post_create, name='all'),
    # path('', views.PostList.as_view(), name='all'),
    # path('<int:num_posts>/', views.load_post, name='load'),

    # path('<pk>', views.PostDetail.as_view(), name='single'),
    path('<pk>', views.post_detail, name='post_detail'),
    # path('delete/<pk>', views.DeletePost.as_view(), name='delete'),

    path('<pk>/delete/', views.delete_post, name='delete'),

    path('<pk>/update/', views.EditPost.as_view(), name='edit'),
    path('posts/in/<slug>', views.SingleGroup.as_view(), name='group'),

    # path('new/', views.CreatePost.as_view(), name='create'),
    # path('add/', views.AddPost, name='add'),

    path('postadd/', views.PostGroup, name='postgroup'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)