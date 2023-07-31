from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea,URLField, NumberInput, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, CountryData
class Detailsform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image','link']
        widgets = {
            'title': TextInput(attrs={
                'class':"form-control text-cemter",
                'placeholder': 'Enter a title for your blog'
            }),
            'body': Textarea(attrs={
                'class':"form-control text-area",
                'placeholder': "Your content goes here...",
                "rows":'8',
                "columns":'20',
            }),
            'link': TextInput(attrs={
                'class':"form-control text-center",
                'placeholder': "Attach any external link.",
            })
        }
        


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control text-center",
                'style': 'width:20rem; font-size:1.3rem;',
                'placeholder': 'Name'
                }),
            'email': EmailInput(attrs={
                'class': "form-control text-center", 
                'style': 'width:20rem;font-size:1.3rem;',
                'placeholder': 'Email'
                }),
            'password1' : PasswordInput(attrs={
                'class' : "form-control",
                'style': 'width:20rem;font-size:1.5rem;',
                'placeholder':'Enter password'
                }),
            'password2' : PasswordInput(attrs={
                'class' : "form-control",
                'style': 'width:20rem;font-size:1.3rem;',
                'placeholder':'Confirm password'
            })
        }

class CountryDataForm(forms.ModelForm):
    class Meta:
        model = CountryData
        fields = ['disease', 'age','name']
        widgets = {
            'name': TextInput(attrs={
                'class':"form-control text-cemter",
                'placeholder': 'Enter Name'
            }),
            'disease': Select(attrs={
                'class':"form-control text-cemter",
                'placeholder': 'Enter disease'
            }),
            'age': NumberInput(attrs={
                'class':"form-control",
                'placeholder': "your age",
            }),
        }

class finddisease(ModelForm):
    class Meta:
        model = CountryData
        fields = ['disease']
        widgets = {
            'disease': Select(attrs={
                'class':"form-control text-cemter",
                'placeholder': 'select disease'
            }),
        }