from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class AddToDoIt(forms.ModelForm):
    userid = None

    class Meta:
        model = ToDoIt
        fields = ['user', 'lvl', 'isfixed', 'title', 'description']
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user_id:
            self.fields['user'].initial = user_id


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Loginer(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')
