from django import forms
from .models import Post
from groups.models import Group


class PostForm(forms.Form):
	message = forms.CharField()
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
		self.fields['group'].queryset = qs
		self.fields['message'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
		self.fields['group'].widget.attrs.update({'class': 'field_select', 'placeholder': ''})





