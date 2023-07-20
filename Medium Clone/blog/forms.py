from blog.models import BlogPost
from django import forms
from tinymce.widgets import TinyMCE
from django.core import validators

from config.validators import min_lenght_3

class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 20}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message="Oops..En az üç karakter olsun")])
    title = forms.CharField(validators=[min_lenght_3])

    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3 :
    #         raise forms.ValidationError('Title must be greater than 3 characters')
    #     return title
