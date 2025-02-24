from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "catalog/widgets/image_widget.html"

class ContactForm(forms.Form):
    title = forms.CharField(max_length=30)
    author = forms.ChoiceField(required=False)
    image = forms.ImageField(label="Image", required=False)
    text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        author = cleaned_data.get('author')
        text = cleaned_data.get('text')
        if not name and not author and not text:
            raise forms.ValidationError('You have to write something!')

    class Meta():
        widgets = {
            'image': ImageWidget,
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Enter text'})
        self.fields['text'].widget.attrs.update({'class': 'field_description', 'placeholder': 'Enter text'})
        self.fields['author'].widget.attrs.update({'class': 'field_select', 'placeholder': 'Select Author'})

        self.fields['image'].widget.attrs.update(widget=forms.ClearableFileInput(attrs={'class': 'field_image'}))
        self.fields['image'].widget.attrs.update({'class': 'field_image', 'placeholder': ''})
        self.fields['image'].widget.clear_checkbox_label = mark_safe(_(
            '<small class="text">Clear</small>'
        ))
        self.fields['image'].widget.initial_text = "CURRENTLY"
        self.fields['image'].widget.input_text = "CHANGE"
 