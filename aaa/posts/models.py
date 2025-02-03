from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ManyToManyField(Group, related_name='posts', blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'message')



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ('id',)

    def __str__(self):
        return self.name


def get_upload_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.user, filename)



class Birdies(models.Model):
    user = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    size_choices = [
        ('Extra-Small', 'Extra-Small'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra-Large', 'Extra-Large'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    tags = TaggableManager(blank=False)
    image = models.ImageField(upload_to=get_upload_path, default="images/blank.jpg", blank=True)
    size = models.CharField(max_length=30, choices=size_choices)

    class Meta:
        verbose_name_plural = "Birds"
        ordering = ['name']

    def __str__(self):
        return self.name

