# blog/forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm): 
  class Meta: 
    model = Post 
    fields = ['title', 'content']
    widgets = {
      'tags': TagWidget()
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['title','content', 'tags']