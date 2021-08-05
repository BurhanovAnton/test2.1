from django.contrib.auth.forms import AuthenticationForm

from authapp.models import BlogUser


class BlogUserLoginForm(AuthenticationForm):
    class Meta:
        model = BlogUser
        fields = ('username', 'password')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field.name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
