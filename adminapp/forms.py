from django import forms

from news.models import News


class NewEditForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.atters['class'] = 'form-control'
                field.help_texts = ''
