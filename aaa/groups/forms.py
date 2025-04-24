from django import forms
from django.db import models
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy
from .models import Group, Comment
from django.forms import ModelForm, FileInput, ImageField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators
from django.contrib.auth import get_user_model
User = get_user_model()




class GroupForm(forms.ModelForm):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(allow_unicode=True, unique=True, blank=True)
	description = models.TextField(blank=True, default='No description yet.')
	description_html = models.TextField(editable=False, default='No description yet.', blank=True)
	members = models.ManyToManyField(User, through='GroupMember')
	

	class Meta():
		model = Group
		fields = ('name', 'description')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Name of the group'})
		self.fields['description'].widget.attrs.update({'class': 'field_description', 'placeholder': 'What is the group about?'})




class CommentForm(forms.ModelForm):
	message = forms.CharField(label='')

	class Meta:
		model = Comment
		fields = ['message']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['message'].widget.attrs.update({'class': 'field_small', 'id': 'id_message', 'placeholder': 'Make a comment'})