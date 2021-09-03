from django import forms

from mane.models import Album, Photo
from news.models import News, Category


class NewEditForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_texts = ''


class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('is_active',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_texts = ''

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('is_active',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_texts = ''


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('is_active',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_texts = ''
