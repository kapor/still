from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.





def get_upload_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.author, filename)


    

class Blog(models.Model):
	author = models.ForeignKey('auth.User', related_name='auth_user', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = TaggableManager(blank=True)
	image = models.ImageField(upload_to=get_upload_path, default="/images/blank.jpg", verbose_name='Image', null=True, blank=True)
	liked = models.ManyToManyField(User, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def approve_comment(self):
		return self.comments_filter(approved_comment=True)

	def get_absolute_url(self):
	    return reverse("blog_detail", kwargs={'pk':self.pk})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Blog"

	# like button
	@property
	def like_count(self):
		return self.liked.all().count()





class Tags(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name