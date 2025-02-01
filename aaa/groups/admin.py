from django.contrib import admin
from . import models
from groups.models import Group, GroupMember
# Register your models here.


class GroupMemberInline(admin.TabularInline):
	model = models.GroupMember

admin.site.register(models.Group)
# admin.site.register(GroupMember)