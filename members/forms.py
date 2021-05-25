from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import fields


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_supervisor = forms.CharField(
        max_length=100,
        widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_stuff = forms.CharField(
        max_length=100,
        widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(
        max_length=100,
        widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',
                  'is_active', 'date_joined', 'is_stuff', 'is_supervisor',
                  'last_login')
