from django.contrib import admin
from posts.models import Product, Birdies, Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Birdies)

