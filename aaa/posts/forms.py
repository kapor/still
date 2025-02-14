from django import forms
from .models import Post
from groups.models import Group


class PostForm(forms.Form):
	# message = forms.CharField(label="Message")
	group = forms.ModelChoiceField(
		label="Group",
		required=True,
		queryset=Group.objects.all(),
		)

	def __init__(self, *args, user=None, **kwargs):
		qs = Group.objects.filter(members=user)
		super().__init__(*args, **kwargs)
		self.fields['group'].queryset = qs


	# def __init__(self, *args, user=None, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.fields['group'].queryset = Group.objects.filter(members=user)

	class Meta:
		model = Post
		fields = ['message', 'group']



