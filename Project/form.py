from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment,BlogPost,Profile



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        
        
        

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=('text',)
        
        
class BlogForm(ModelForm):
    class Meta:
        model=BlogPost
        fields=('category','title','content','featured_image')
        
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_img']