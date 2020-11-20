from django import forms

class LoginDetails(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)