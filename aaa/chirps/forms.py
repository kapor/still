from django import forms
from .models import Post
from groups.models import Group
from django.forms import ModelForm, FileInput, ImageField, ModelChoiceField, ClearableFileInput
from django.contrib.auth import get_user_model
User = get_user_model()




class post_group(forms.Select):
    template_name = 'widgets/post_group.html'



class file_input_initial(forms.ClearableFileInput):
    template_name = 'widgets/file_input_initial.html'


class file_input_edit(forms.ClearableFileInput):
    template_name = 'widgets/file_input_edit.html'


    

class PostForm(forms.ModelForm):
	group = forms.ModelChoiceField(
		label="Group",
		required=True,
		queryset=Group.objects.all(),
		)
	image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'field_image',}))

	class Meta:
		model = Post
		fields = ['message', 'group', 'image']

	def __init__(self, *args, user=None, **kwargs):
		qs = Group.objects.filter(members=user)
		super().__init__(*args, **kwargs)


		self.fields['message'].widget.attrs.update({
			'class': 'field_description', 
			# 'placeholder': 'What are you going to say?',
			'id': 'id_message'
		})

		self.fields['group'].queryset = qs
		self.fields['group'].widget.attrs.update({
			'class': 'field_select', 
			# 'placeholder': 'Select from your groups', 
			'id': 'id_group'
		})

		self.fields['image'].widget.attrs.update({
			'class': 'field_image', 
			'placeholder': '',
			'id': 'id_image'
		})

		for field in self.fields.values():
			self.fields['image'].required = False


# class PhotoForm(forms.ModelForm):
# 	class Meta:
# 		model = Photo
# 		fields = ['image']









class PostFormGroup(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['user', 'message',] 

	def __init__(self, *args, group=None, **kwargs):
		super().__init__(*args, **kwargs)
		if group:
			self.initial['group'] = group
			self.fields['group'].widget = forms.HiddenInput() 




class EditForm(forms.ModelForm):


	class Meta:
		model = Post
		fields = ['message',]
		exclude = ['group',]

	def __init__(self, *args, user=None, **kwargs):
		# qs = Group.objects.filter(members=user)
		super().__init__(*args, **kwargs)

		self.fields['message'].widget.attrs.update({
			'class': 'field_description', 
			'id': 'id_message'
		})


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if 'instance' in kwargs and kwargs['instance']:  # Check if editing an existing post
			if not kwargs['instance'].group: #Check if group is already set
				default_group = Group.objects.first()  # Or however you get your default group
				self.fields['group'].initial = default_group





