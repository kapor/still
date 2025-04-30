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


class Profile(models.Model):
	user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)
	picture = models.ImageField(upload_to=get_upload_path, blank=True)

	def __str__(self):
   		return f"{self.user.username}'s profile"

	class Meta:
		verbose_name_plural = "Profiles"