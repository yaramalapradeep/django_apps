from django import forms
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField( max_length=100)
    password = forms.CharField( max_length=20, widget=forms.PasswordInput)

class AddForm(forms.Form):
    STATUS_CHOICES =(
    ("START", "START"),
    ("IN-PROGRESS", "IN-PROGRESS"),
    ("DONE", "DONE"),
    )

    title = forms.CharField()
    details=forms.CharField()
    status=forms.ChoiceField(choices = STATUS_CHOICES)
class UpdateForm(forms.Form):
    STATUS_CHOICES =(
    ("START", "START"),
    ("IN-PROGRESS", "IN-PROGRESS"),
    ("DONE", "DONE"),
    )
    status=forms.ChoiceField(choices = STATUS_CHOICES)
class SignupForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
