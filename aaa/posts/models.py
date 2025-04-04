from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings


import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()



def get_upload_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.user, filename)


class Post(models.Model):
    user = models.ForeignKey(User, related_name='post_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(unique=False)
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=get_upload_path, default="/images/blank.jpg", verbose_name='Image', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']







