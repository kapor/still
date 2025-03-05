from django import forms
from .models import Post
from groups.models import Group






class post_group(forms.Select):
    template_name = 'widgets/post_group.html'




class PostForm(forms.Form):
	message = forms.CharField(widget=forms.Textarea)
	group = forms.ModelChoiceField(
		label="Group",
		required=True,
		queryset=Group.objects.all(),
		)


	class Meta:
		model = Post
		fields = ['message', 'group']

	def __init__(self, *args, user=None, **kwargs):
		qs = Group.objects.filter(members=user)
		super().__init__(*args, **kwargs)
		self.fields['message'].widget.attrs.update({'class':'field_description'})
		self.fields['group'].queryset = qs
		self.fields['group'].widget.attrs.update({'class': 'field_select', 'placeholder': ''})






# class PostFormGroup(forms.ModelForm):
# 	message = forms.CharField()
# 	group = forms.ModelChoiceField(label="group", required=False, queryset=Group.objects.all(), widget=post_group())



# 	class Meta:
# 		model = Post
# 		fields = ['message', 'group']

# 	def __init__(self, *args, user=None, **kwargs):
# 		qs = Group.objects.filter(members=user)
# 		super().__init__(*args, **kwargs)
# 		self.fields['group'].queryset = qs
# 		self.fields['message'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
# 		self.fields['group'].widget.attrs.update({'class': 'field_select', 'placeholder': ''})




# 	def __init__(self, *args, **kwargs):
# 		user = kwargs.pop('user', None)  # Get the user from kwargs, if provided
# 		super().__init__(*args, **kwargs)
# 		if user:
# 			self.instance.group = user # Automatically set the foreign key




class PostFormGroup(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['user', 'message',] 

	def __init__(self, *args, group=None, **kwargs):
		super().__init__(*args, **kwargs)
		if group:
			self.initial['group'] = group
			self.fields['group'].widget = forms.HiddenInput() 








