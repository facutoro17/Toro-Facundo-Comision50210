from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuario(UserCreationForm):
   
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
    
class FormularioEditar(UserCreationForm):
   
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

class FormularioAvatar(forms.ModelForm):

    class Meta:
        
        model = Avatar
        fields = ["imagen"]