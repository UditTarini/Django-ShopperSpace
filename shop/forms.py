from allauth.account.forms import LoginForm
from django import forms

input = forms.CharField(
            widget=forms.TextInput(attrs={'class':'form-control'}))