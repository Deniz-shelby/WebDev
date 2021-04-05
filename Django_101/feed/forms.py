from django import forms
from django.forms.fields import FileField

class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label='Description')