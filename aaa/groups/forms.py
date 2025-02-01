from django import forms
from django.db import models
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from .models import Group
from django.forms import ModelForm, FileInput, ImageField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators
from django.contrib.auth import get_user_model
User = get_user_model()


class GroupForm(forms.ModelForm):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
	description = models.TextField(blank=True, default='')
	description_html = models.TextField(editable=False, default='', blank=True)
	members = models.ManyToManyField(User, through='GroupMember')
	class Meta():
		model = Group
		fields = ('name', 'slug', 'description')
