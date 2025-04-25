from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse

from django.contrib.auth import get_user_model
User = get_user_model()






def get_upload_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.user, filename)

class Blog(models.Model):
	user = models.ForeignKey(User, related_name='blog_user', null=False, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	message = models.TextField(unique=False)
	liked = models.ManyToManyField(User, blank=True)
	created_at = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = TaggableManager(blank=True)
	image = models.ImageField(upload_to=get_upload_path, verbose_name='Image', null=True, blank=True)

	def __str__(self):
		return self.title

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	# like button
	@property
	def like_count(self):
		return self.liked.all().count() 

	def get_absolute_url(self):
		return reverse("blog:blog_detail", kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-created_at']
		verbose_name_plural = "Blog"




class Tags(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name