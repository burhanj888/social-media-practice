from django import forms
from .models import Post


class HomeForm(forms.ModelForm):
    caption = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a caption'
        }
    ))

    image = forms.FileField(required=False ,widget=forms.FileInput(
        attrs={
            'class': 'form-control',
            'type': 'file'
        }
    ))

    class Meta:
        model = Post
        fields = ('image','caption')