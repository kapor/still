from django.db import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
from django.db.models import F
from taggit.managers import TaggableManager
from django.views.generic import ListView
from django.contrib.auth.models import User
from blog.models import Tags
from django.urls import reverse
from django.contrib import admin
from pathlib import Path
import os
# Create your models here.




def get_upload_path(instance, filename):
	return 'shelves/{0}/{1}'.format(instance.user.username, filename)
	



class Shelves(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey('auth.User', related_name='shelf_user', on_delete=models.CASCADE)
	title = models.CharField(max_length=1000, blank=True, null=True)
	author = models.CharField(max_length=1000, blank=True, null=True)
	year = models.IntegerField(blank=True, null=True)
	type = models.CharField(max_length=500, blank=True, null=True)
	publisher = models.CharField(max_length=500, blank=True, null=True)
	artist = models.CharField(max_length=500, blank=True, null=True)
	quality = models.CharField(max_length=500, blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=20, blank=True, null=True, default='.00')
	location = models.CharField(max_length=500, blank=True, null=True)
	genre = models.CharField(max_length=500, blank=True, null=True)
	tags = TaggableManager(blank=True)
	weight = models.FloatField(blank=True, null=True, default='0')
	pages = models.IntegerField(blank=True, null=True, default='0')
	isbn = models.CharField(max_length=500, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to=get_upload_path, default="shelves/blank.jpg", blank=True)
	notes = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now=True)
	liked = models.ManyToManyField(User, blank=True, related_name='shelf_liked')

	class Meta:
		verbose_name_plural = "Shelves"
		ordering = ['-created_at']

	def __str__(self):
		return self.title

	def get_queryset(self):
		return super().get_queryset().filter(user=self.request.user)

	def get_absolute_url(self):
		return reverse("shelf:detail", kwargs={'pk':self.pk})

	# like button
	@property
	def like_count(self):
		return self.liked.all().count() 


	def save(self, *args, **kwargs):
		self.clean()
		super().save(*args, **kwargs)


