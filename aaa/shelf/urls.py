from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from shelf import views
from . import views


app_name = 'shelf'

urlpatterns = [

    path('shelf/', views.ShelfListView.as_view(), name='shelf'),
    # path('entry/', views.ShelfEntry, name='entry'),
    # modal
    path('add/', views.ShelfAdd, name='add'),
    path('shelf/<int:pk>/', views.ShelfDetailView.as_view(), name='detail'),
    path('shelf/<int:pk>/edit/', views.Edit_Item.as_view(), name='edit'),
    path('shelf/<int:pk>/delete', views.Delete_Item.as_view(), name='delete'),

    path('shelf/', views.SearchView.as_view(), name='search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

