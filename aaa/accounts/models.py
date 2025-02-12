from django.db import models
from django.contrib import admin, auth
from django.db import models
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import URLValidator
from pathlib import Path
import os



def get_upload_path(instance, filename):
    return 'profile_pics/{0}/{1}'.format(instance.user.username, filename)


# Create your models here.
class UserInfo(auth.models.User, auth.models.PermissionsMixin):
	user = models.OneToOneField('auth.User', related_name='acct_user', on_delete=models.CASCADE)
	picture = models.ImageField(upload_to=get_upload_path, default="profile_pics/blank.jpg", blank=True)
	
	def __str__(self):
   		return self.user.username

	class Meta:
		# managed = False
		# ordering = ('id',)
		verbose_name_plural = "User_Info"





