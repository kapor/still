from django.conf.urls.static import static, settings
from django.contrib import admin
from django.urls import include, path
from groups import urls
from . import views
from .views import ( 
    list_post_create,
    like_unlike_post,
    post_detail,
    post_detail_data,
    delete_post,
    edit_post,
)


app_name = 'posts'

urlpatterns = [
    path('', views.list_post_create, name='all'),
    path('like_unlike/', like_unlike_post, name='like_unlike'),

    path('<pk>', views.post_detail, name='post_detail'),
    path('<pk>/data/', views.post_detail_data, name='post_detail_data'),
    path('<pk>/delete/', views.delete_post, name='delete'),
    # path('<pk>/update/', views.edit_post, name='edit'),
    path('<pk>/update/', views.edit_post, name='edit'),

    # path('posts/in/<slug>', views.SingleGroup.as_view(), name='group'),


    path('postadd/', views.PostGroup, name='postgroup'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)