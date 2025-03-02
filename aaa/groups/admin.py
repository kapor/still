from django.contrib import admin
from . import models
from groups.models import Group, GroupMember, Comment
# Register your models here.


class GroupMemberInline(admin.TabularInline):
	model = models.GroupMember

admin.site.register(models.Group)
admin.site.register(models.Comment)
# admin.site.register(GroupMember)