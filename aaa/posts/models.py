from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()



def get_upload_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.user.username, filename)


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(unique=False)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=get_upload_path, default="posts/blank.jpg", blank=True)
    liked = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        # constraints = [
        #     models.UniqueConstraint(fields=['user', 'message', 'group'], name='unique_user_message_group')
        # ]


    # like button
    @property
    def like_count(self):
        return self.liked.all().count()












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



