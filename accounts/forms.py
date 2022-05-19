from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(label=_("Email"))

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]