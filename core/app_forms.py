from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email

from core import app_validation


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(validators=[app_validation.validate_username])
    email = forms.EmailField(validators=[validate_email, app_validation.validate_unique("email", User)])

    class Meta:
        model = get_user_model()
        fields = ['password1', 'password2']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.username = self.cleaned_data['username']
        usuario.email = self.cleaned_data['email']

        if commit:
            usuario.save()

        return usuario
