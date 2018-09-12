from django.contrib.auth.models import User
from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    content = forms.CharField(label="content", widget=forms.Textarea)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password"]