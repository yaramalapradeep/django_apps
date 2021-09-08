from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='user name', max_length=100)
    password = forms.CharField(label='password', max_length=20, widget=forms.PasswordInput)

class AddForm(forms.Form):
    STATUS_CHOICES =(
    ("START", "START"),
    ("PROGRESS", "PROGRESS"),
    ("DONE", "DONE"),
    )

    title = forms.CharField()
    details=forms.CharField()
    status=forms.ChoiceField(choices = STATUS_CHOICES)
class UpdateForm(forms.Form):
    STATUS_CHOICES =(
    ("START", "START"),
    ("PROGRESS", "PROGRESS"),
    ("DONE", "DONE"),
    )
    status=forms.ChoiceField(choices = STATUS_CHOICES)
