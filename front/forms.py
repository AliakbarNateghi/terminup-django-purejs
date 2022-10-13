from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=256,
                             widget=forms.EmailInput(attrs={'placeholder': 'ustink@gmail.com', 'size': "40",
                                                            'class': "form-control form-control-lg"}))
    # phone = forms.PhoneNumberField()

    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': '**********'}))

    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': '**********'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control form-control-lg",
                'placeholder': 'ali_akbar'
            })
        }
