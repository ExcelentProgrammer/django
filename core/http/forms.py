#####################
# Project base forms
#####################
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from core.http.models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'desc': CKEditor5Widget(),
        }
        fields = '__all__'
