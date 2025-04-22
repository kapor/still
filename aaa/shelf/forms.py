from django import forms
from .models import Shelves, get_upload_path
from django.forms import ModelForm, FileInput, ImageField, ModelChoiceField
from taggit.forms import TagField, TagWidget
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
    tags = TagField(label="Tags", required=False, widget=TagWidget())
    description = forms.Textarea()
    image = forms.ImageField(label="Image", required=False)
    botcat = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_title'})
        self.fields['author'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_author'})
        self.fields['year'].widget.attrs.update({'class': 'field_int', 'placeholder': '', 'id': 'id_year'})
        self.fields['tags'].widget.attrs.update({'class': 'field_char', 'placeholder': 'A comma-separated list of tags', 'id': 'id_tags'})
        self.fields['description'].widget.attrs.update({'class': 'field_description', 'placeholder': '', 'id': 'id_description'})
        self.fields['image'].widget.attrs.update({'class': 'field_image', 'id': 'id_image'})
        for field in self.fields.values():
            self.fields['image'].required = False

    class Meta():
        model = Shelves
        fields = ('title', 'author', 'tags', 'description', 'image',)
        exclude = ('year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'genre', 'weight', 'pages', 'isbn', 'notes',)

    def clean(self):
        all_clean = super().clean()



class ShelfUpdateForm(forms.ModelForm):
    title = forms.CharField(label="Title", max_length=500, required=True)
    author = forms.CharField(label="Author", max_length=500, required=False)
    year = forms.IntegerField(label="Year", required=False)
    type = forms.CharField(label="Type", max_length=500, required=False)
    publisher = forms.CharField(label="Publisher", max_length=500, required=False)
    artist = forms.CharField(label="Artist", max_length=500, required=False)
    quality = forms.CharField(label="Quality", max_length=500, required=False)
    price = forms.DecimalField(label="Price", required=False)
    location = forms.CharField(label="Location", max_length=500, required=False)
    tags = TagField(label="Tags", required=False, widget=TagWidget())
    #genre = forms.CharField(label="Genre", max_length=500, required=False)
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
        self.fields['title'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_title'})
        self.fields['author'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_author'})
        self.fields['year'].widget.attrs.update({'class': 'field_int', 'placeholder': '', 'id': 'id_year'})
        self.fields['type'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_type'})
        self.fields['publisher'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_publisher'})
        self.fields['artist'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_artist'})
        self.fields['quality'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_quality'})
        self.fields['price'].widget.attrs.update({'class': 'field_decimal', 'id': 'id_price'})
        self.fields['location'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_location'})
        # self.fields['genre'].widget.attrs.update({'class': 'field_char', 'placeholder': ''})
        self.fields['tags'].widget.attrs.update({'class': 'field_char', 'placeholder': 'A comma-separated list of tags', 'id': 'id_tags'})
        self.fields['weight'].widget.attrs.update({'class': 'field_float', 'placeholder': '', 'id': 'id_weight'})
        self.fields['pages'].widget.attrs.update({'class': 'field_int', 'placeholder': '', 'id': 'id_pages'})
        self.fields['isbn'].widget.attrs.update({'class': 'field_char', 'placeholder': '', 'id': 'id_isbn'})
        self.fields['description'].widget.attrs.update({'class': 'field_description', 'placeholder': '', 'id': 'id_description'})
        self.fields['notes'].widget.attrs.update({'class': 'field_description', 'placeholder': '', 'id': 'id_notes'})
        self.fields['image'].widget.attrs.update({'class': 'field_image', 'id': 'id_image'})
        for field in self.fields.values():
            self.fields['image'].required = False


    class Meta():
        model = Shelves
        fields = ('title', 'author' , 'year', 'type', 'publisher', 'artist', 'quality', 'price', 'location', 'tags', 'weight', 'pages', 'isbn', 'description', 'notes', 'image',)
        # exclude = ('tags', )

    def clean(self):
        all_clean = super().clean()







