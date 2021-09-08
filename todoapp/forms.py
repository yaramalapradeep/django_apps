from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Your user name', max_length=100)
    password = forms.CharField(label='Your password', max_length=20, widget=forms.PasswordInput)

class AddForm(forms.Form):
    STATUS_CHOICES =(
    ("START", "START"),
    ("PROGRESS", "PROGRESS"),
    ("DONE", "DONE"),
    )
    content = forms.CharField()
    status=forms.ChoiceField(choices = STATUS_CHOICES)
