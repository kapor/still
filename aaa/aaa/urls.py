from django.contrib import admin
from django.conf.urls.static import static, settings
from django.urls import include, path
from . import views
    
app_name = 'aaa'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('profiles/', include('profiles.urls', namespace="profiles")),
    path('posts/', include('posts.urls', namespace="posts")),
    path('chirps/', include('chirps.urls', namespace="chirps")),
    path('users/', include('profiles.urls', namespace="profiles")),
    path('blog/', include('blog.urls', namespace="blog")),
    path('shelf/', include('shelf.urls', namespace="shelf")),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('groups/', include('groups.urls', namespace='groups')),

    path("", views.Activity.as_view(), name="home"),
    path('results', views.Activity.SearchView.as_view(), name='index_search'),
    path('user/<username>', views.User_Activity, name='for_user'),


    path('contact/', include('contact.urls', namespace="contact")),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

