from django.contrib import admin
from django.conf.urls.static import static, settings
from django.urls import include, path
from . import views

app_name = 'profiles'

urlpatterns = [


    path('<username>', views.profile_view, name='for_user'),
    # path('user/<username>', views.User_Activity, name='for_user'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)