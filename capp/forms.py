from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Question, Comment, Session



class ProfileForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create Post
    '''
    class Meta:
        model = Profile

        fields = ['first_name','last_name', 'email', 'phone_number', 'addiction']

class QuestionForm(forms.ModelForm):
    '''
    classs that creates profile update form
    '''
    class Meta:
        model = Question
        fields = ['topic']

class CommentForm(forms.ModelForm):
    '''
    class that creates the comment form
    '''
    class Meta:
        model = Comment
        fields = ['opinion']
