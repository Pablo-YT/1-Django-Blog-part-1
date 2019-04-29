from django.shortcuts import render
from django.contrib.auth import login
from django.forms import CharField, PasswordInput
from django import forms
from .models import Article


class LoginForm(forms.Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())


class articleform(forms.ModelForm):
    title = forms.CharField(max_length=250)
    body = forms.CharField(max_length=244, widget=forms.Textarea)
    draft = forms.ChoiceField(label="Draft",
                                initial='',
                                widget=forms.Select(),
                                required=True)
    class Meta():
        model = Article
        fields = ('title', 'body', 'draft')