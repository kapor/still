from django.db import models
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from django.utils import timezone

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()



class Group(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
	description = models.TextField(blank=True)
	description_html = models.TextField(editable=False, default='No description yet.', blank=True)
	members = models.ManyToManyField(User, through='GroupMember')

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		self.description_html = misaka.html(self.description)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
	    return reverse("groups:single", kwargs={'slug':self.slug})

	class Meta:
		ordering = ['name']


class GroupMember(models.Model):
	group = models.ForeignKey(Group, related_name='group_member', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

	class Meta:
		unique_together = ('group', 'user')



class Comment(models.Model):
	group = models.ForeignKey(Group, related_name='comment_group', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now=True, blank=True, null=True)

	def get_absolute_url(self):
	    return reverse("groups:single", kwargs={'slug':self.slug})

	def __str__(self):
		return self.message

	class Meta:
		ordering = ['-created_at']