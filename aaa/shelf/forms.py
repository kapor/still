from django import forms
from .models import Shelves, get_upload_path
from django.forms import ModelForm, FileInput, ImageField, ModelChoiceField
from taggit.forms import TagField
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core import validators



class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update({'class': 'field_small', 'placeholder': ''})



class file_input_initial(forms.ClearableFileInput):
    template_name = 'widgets/file_input_initial.html'


class file_input_edit(forms.ClearableFileInput):
    template_name = 'widgets/file_input_edit.html'


class ShelfEntryForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=500, required=True)
    author = forms.CharField(label="Author", max_length=500, required=False)
    year = forms.IntegerField(label="Year", required=False)
    type = forms.CharField(label="Type", max_length=500, required=False)
    publisher = forms.CharField(label="Publisher", max_length=500, required=False)
    artist = forms.CharField(label="Artist", max_length=500, required=False)
    quality = forms.CharField(label="Quality", max_length=500, required=False)
    price = forms.DecimalField(label="Price", required=False)
    location = forms.CharField(label="Location", max_length=500, required=False)
    # genre = forms.CharField(label="Genre", max_length=500, required=False)
    weight = forms.FloatField(label="Weight", required=False)
    pages = forms.IntegerField(label="Pages", required=False)
    isbn = forms.CharField(label="ISBN", required=False)
    description = forms.Textarea()
    notes = forms.Textarea()
    image = forms.ImageField(label="Image", required=False)
    update = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    botcat = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['author'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['year'].widget.attrs.update({'class': 'field_int', 'placeholder': ''})
        self.fields['type'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['publisher'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['artist'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['quality'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['price'].widget.attrs.update({'class': 'field_decimal', 'placeholder': ''})
        self.fields['location'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        # self.fields['genre'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['tags'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Comma-separated'})
        self.fields['weight'].widget.attrs.update({'class': 'field_float', 'placeholder': ''})
        self.fields['pages'].widget.attrs.update({'class': 'field_int', 'placeholder': ''})
        self.fields['isbn'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['description'].widget.attrs.update({'class': 'field_description', 'placeholder': ''})
        self.fields['notes'].widget.attrs.update({'class': 'field_description', 'placeholder': ''})
        self.fields['image'].widget.attrs.update({'class': 'field_image'})
        for field in self.fields.values():
            self.fields['image'].required = False


    class Meta():
        model = Shelves
        fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'tags', 'weight', 'pages', 'isbn', 'description', 'notes', 'image')

    def clean(self):
        all_clean = super().clean()




class ShelfEntryEdit(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=500, required=True)
    author = forms.CharField(label="Author", max_length=500, required=False)
    year = forms.IntegerField(label="Year", required=False)
    type = forms.CharField(label="Type", max_length=500, required=False)
    publisher = forms.CharField(label="Publisher", max_length=500, required=False)
    artist = forms.CharField(label="Artist", max_length=500, required=False)
    quality = forms.CharField(label="Quality", max_length=500, required=False)
    price = forms.DecimalField(label="Price", required=False)
    location = forms.CharField(label="Location", max_length=500, required=False)
    # genre = forms.CharField(label="Genre", max_length=500, required=False)
    weight = forms.FloatField(label="Weight", required=False)
    pages = forms.IntegerField(label="Pages", required=False)
    isbn = forms.CharField(label="ISBN", required=False)
    description = forms.Textarea()
    notes = forms.Textarea()
    image = forms.ImageField(label="Image", required=False, widget=file_input_edit())
    update = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    botcat = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['author'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['year'].widget.attrs.update({'class': 'field_int', 'placeholder': ''})
        self.fields['type'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['publisher'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['artist'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['quality'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['price'].widget.attrs.update({'class': 'field_decimal', 'placeholder': ''})
        self.fields['location'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        # self.fields['genre'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['tags'].widget.attrs.update({'class': 'field_char', 'placeholder': 'Comma-separated'})
        self.fields['weight'].widget.attrs.update({'class': 'field_float', 'placeholder': ''})
        self.fields['pages'].widget.attrs.update({'class': 'field_int', 'placeholder': ''})
        self.fields['isbn'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['description'].widget.attrs.update({'class': 'field_description', 'placeholder': ''})
        self.fields['notes'].widget.attrs.update({'class': 'field_description', 'placeholder': ''})
        self.fields['image'].widget.attrs.update({'class': 'field_image'})
        for field in self.fields.values():
            self.fields['image'].required = False


    class Meta():
        model = Shelves
        fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'tags', 'weight', 'pages', 'isbn', 'description', 'notes', 'image')


    def clean(self):
        all_clean = super().clean()