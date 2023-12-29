from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Project, Task, Post, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class Form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.IntegerField()
    adress = forms.CharField()
    photo = forms.FileField()
    date = forms.DateField(widget=forms.SelectDateWidget())


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['text']


class TestForm(forms.Form):
    name = forms.CharField()


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'status', 'deadline']
        widgets ={'text': forms.TextInput(attrs={'id': 'text'}),
            "status": forms.CheckboxInput(attrs={'id':'status'}),
            "deadline": forms.DateInput(attrs={'id':'deadline'})}




class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'ÐÐ¾ÑÑÐº...'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']



