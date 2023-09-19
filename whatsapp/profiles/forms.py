from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput())


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=20)
    about_yourself = forms.CharField(widget=forms.Textarea())


class MessagesForm(forms.Form):
    message_text = forms.CharField(widget=forms.Textarea())
