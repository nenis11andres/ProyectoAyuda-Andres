from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    rol = forms.ChoiceField(choices=Usuario.ROLES)
    
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'rol']
