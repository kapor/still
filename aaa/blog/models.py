from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.





def get_upload_path(instance, filename):
    return 'images/{0}/{1}'.format(instance.author, filename)


    

class Blog(models.Model):
	author = models.ForeignKey('auth.User', related_name='auth_user', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = TaggableManager(blank=True)
	# tags = models.ManyToManyField(to='blog.Tags', related_name='blog_tags', blank=True)
	image = models.ImageField(upload_to=get_upload_path, default="/images/blank.jpg", verbose_name='Image', null=True, blank=True)

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






class Tags(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name