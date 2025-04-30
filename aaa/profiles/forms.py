from django import forms
from .models import Profile




class ProfileForm(forms.ModelForm):
    class Meta: 
            model = Profile
            fields = ('bio', 'picture')

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['bio'].widget.attrs.update({
            'class': 'field_description_2', 
            'id': 'id_bio'
        })

        self.fields['picture'].widget.attrs.update({
            'class': 'field_image_2',
            'id': 'id_image'
        })


# class ClearImageForm(forms.ModelForm):
#     delete_image = forms.BooleanField(required=False, widget=forms.CheckboxInput)

#     class Meta:
#         model = Profile
#         fields = ['picture']