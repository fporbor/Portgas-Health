from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=False, label="Nombre")
    last_name = forms.CharField(max_length=150, required=False, label="Primer apellido")
    apellido2 = forms.CharField(max_length=150, required=False, label="Segundo apellido")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")
    fecha_nacimiento = forms.DateField(
        required=False,
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Usuario
        fields = [
            'username', 'first_name', 'last_name', 'apellido2',
            'email', 'telefono', 'fecha_nacimiento',
            'password1', 'password2'
        ]