from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from shelf import views
from . import views


app_name = 'shelf'

urlpatterns = [


    path('', views.shelf_list_create, name='shelf'),

    path('<int:pk>/', views.shelf_detail, name='detail'),
    path('like_unlike/', views.like_unlike_shelf, name='like_unlike'),

    path('<int:pk>/data/', views.shelf_detail_data, name='data'),

    path('<int:pk>/delete/', views.shelf_delete, name='delete'),
    path('<int:pk>/update/', views.shelf_edit, name='edit'),

    path('search/', views.shelf_search, name='search'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

