# from django import forms

# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=200)
#     content = forms.CharField(label="내용", widget = forms.Textarea)

from second.models import Post
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title' : _('제목'),
            'content' : _('내용'),
        }