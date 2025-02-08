from django import forms
from .models import Post


class PostForm(forms.Form):
	message = forms.CharField()
	group = forms.ChoiceField(choices=[])

	class Meta:
		model = Post
		fields = ('message', 'group')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['group'].choices = [(group.name) for group in Group.objects.all()]