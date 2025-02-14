from django import forms
from django.db import models
from .models import Blog, Tags, get_upload_path
from django.forms import ModelForm, FileInput, ImageField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators
from django_select2 import forms as s2forms
from django_select2.forms import Select2MultipleWidget




class CustomClearableFileInput(forms.ClearableFileInput):
    template_name = 'custom_clearable_file_input.html'


class BlogForm(forms.ModelForm):
	image = forms.ImageField(label="Image", required=False)
	title = forms.CharField(max_length=200)
	image = forms.ImageField(label="Image", required=False)
	update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

	class Meta():
		model = Blog
		fields = ('title', 'author', 'text', 'tags', 'image')

		widgets = {
			'title':forms.TextInput(attrs={'class':'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image': CustomClearableFileInput,
		}





class BlogUpdate(forms.ModelForm):
	title = forms.CharField(max_length=200)
	image = forms.ImageField(label="Image", required=False)
	update = forms.BooleanField(widget=forms.HiddenInput, initial=True)

	class Meta():
		model = Blog
		fields = ('title', 'author', 'text', 'tags', 'image')
		widgets = {
			'title':forms.TextInput(attrs={'class':'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image': CustomClearableFileInput,
		}