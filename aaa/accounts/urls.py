from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . import views
from .views import LoginModal

app_name = 'accounts'

urlpatterns = [

	path("login/", auth_views.LoginView.as_view(template_name='reg/login.html'), name="login"),
	path("login/", views.LoginModal.as_view(template_name='reg/login_modal.html'), name="login_modal"),
	path("logout/", auth_views.LogoutView.as_view(), name="logout"),

	path("signup/", views.SignUp.as_view(template_name='reg/signup.html'), name="signup"),
	

	# path("profile/", views.user_info_view, name="profile"),


]
