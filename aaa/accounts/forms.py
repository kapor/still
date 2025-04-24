from django import forms
from django.forms import ModelForm 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model



def check_length(value):
    if len(value) <= 1:
        raise ValidationError("Needs more than one character.")
    if not value:
        raise ValidationError("This field cannot be blank.")


class UserForm(UserCreationForm):
	photo = forms.ImageField(label="Image", required=False)

	class Meta: 
		fields = ('username', 'email', 'password1', 'password2', 'photo')
		model = get_user_model()

	#another way to add labels to the fields
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Username'})
		self.fields['email'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Email'})
		self.fields['password1'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Password'})
		self.fields['password2'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Password again'})
		self.fields['photo'].widget.attrs.update({'class': 'field_image', 'id': 'id_photo'})
		for field in self.fields.values():
			self.fields['photo'].required = False











# class UserForm1(forms.ModelForm):
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

# 	class Meta():
# 		model = User
# 		fields = ('username','email','password')

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise ValidationError(
#                 "Passwords do not match."
#             )
#         return cleaned_data


# class UserForm2(forms.ModelForm):
# 	# website = forms.URLField(initial="https://") 
# 	# website=forms.CharField(required=False, initial="https://") 

# 	class Meta():
# 		model = UserInfo
# 		fields = ('picture',)






