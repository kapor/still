from django.conf import settings
from django.conf.urls.static import static, settings
from django.urls import path, include
from . import views




urlpatterns = [

    path('', views.ShelfListView.as_view(), name='ShelfList'),

]