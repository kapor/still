from django.contrib import admin
from django.conf.urls.static import static, settings
from django.urls import include, path
from . import views
from .views import IndexLoad, load_more

app_name = 'aaa'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls', namespace="posts")),
    path('updates/', include(('blog.urls', 'blog'), namespace='updates')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('groups/', include('groups.urls', namespace='groups')),
    # path("", views.IndexView.as_view(template_name='index.html'), name="home"),
    path("", views.Activity.as_view(), name="home"),
    path('results', views.Activity.SearchView.as_view(), name='index_search'),
    path('user/<username>', views.User_Activity, name='for_user'),


    path('index_load/', IndexLoad, name='index_load'),
    path('load/', load_more, name='load'),

    path('', include('blog.urls')),
    path('', include(('shelf.urls', 'shelf'), namespace='shelf')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

