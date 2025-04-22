from django import forms
from django.db import models
from .models import Blog, Tags, get_upload_path
from django.forms import ModelForm, FileInput, ImageField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators
from django_select2 import forms as s2forms
from django_select2.forms import Select2MultipleWidget
from django.forms import widgets
from taggit.forms import TagField, TagWidget








class file_input_initial(forms.ClearableFileInput):
    template_name = 'widgets/file_input_initial.html'




class file_input_edit(forms.ClearableFileInput):
    template_name = 'widgets/file_input_edit.html'





class BlogForm(forms.ModelForm):
	title = forms.CharField(max_length=200)
	image = forms.ImageField(required=False, widget=file_input_edit({'class': 'field_image'}))
	update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

	class Meta():
		model = Blog
		fields = ('title', 'message', 'tags', 'image',)
		exclude = ('user', 'published_date', 'liked',)


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None) # Get user from views.py
		super().__init__(*args, **kwargs)

		self.fields['title'].widget.attrs.update({
		'class': 'field_char', 
		'placeholder': '', 
		'id': 'id_title',
		})

		self.fields['message'].widget.attrs.update({
		'class': 'field_description', 
		'placeholder': '',
		'id': 'id_message',
		})


		self.fields['tags'].widget.attrs.update({
		'class': 'field_char', 
		'placeholder': 'A comma-separated list of tags.',
		})

		self.fields['image'].widget.attrs.update({
		'class': 'field_image',
		'id': 'id_image',
		})
		for field in self.fields.values():
			self.fields['image'].required = False








class BlogUpdate(forms.ModelForm):
	title = forms.CharField(max_length=200)
	image = forms.ImageField(required=False, widget=file_input_edit({'class': 'field_image'}))
	update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

	class Meta():
		model = Blog
		fields = ('title', 'message', 'tags', 'image')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['title'].widget.attrs.update({
		'class': 'field_char', 
		'id': 'id_title',
		})

		self.fields['message'].widget.attrs.update({
		'class': 'field_description', 
		'id': 'id_message',
		})

		self.fields['tags'].widget.attrs.update({
		'class': 'field_char', 
		'placeholder': 'A comma-separated list of tags.',
		})

		self.fields['image'].widget.attrs.update({
		'class': 'field_image',
		'id': 'id_image',
		})

		for field in self.fields.values():
			self.fields['image'].required = False





