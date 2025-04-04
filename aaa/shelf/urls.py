from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from shelf import views
from . import views


app_name = 'shelf'

urlpatterns = [

    # path('', views.ShelfListView.as_view(), name='shelf'),
    # path('entry/', views.ShelfEntry, name='entry'),
    path('', views.shelf_list_create, name='shelf'),
    path('<int:pk>/', views.shelf_detail_view, name='detail'),
    # path('<int:pk>/', views.Edit_Item.as_view(), name='edit'),
    path('<int:pk>/data', views.shelf_detail_data, name='data'),
    path('<int:pk>/delete', views.Delete_Item.as_view(), name='delete'),

    path('search/', views.SearchView.as_view(), name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

