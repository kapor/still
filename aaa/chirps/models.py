from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
from django.conf import settings


from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()



def get_upload_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.user, filename)


class Post(models.Model):
    user = models.ForeignKey(User, related_name='chirp_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(unique=False)
    liked = models.ManyToManyField(User, blank=True)
    group = models.ForeignKey(Group, related_name="chirp_group", null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField(upload_to=get_upload_path, verbose_name='Image', null=True, blank=True)

    def __str__(self):
        return self.message

    # like button
    @property
    def like_count(self):
        return self.liked.all().count() 

    def get_absolute_url(self):
        return reverse("chirps:single", kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']




# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=get_upload_path)
#     created_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.post.message}-{self.pk}"