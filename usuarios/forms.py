from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'placeholder': 'Usuario',
            'autocomplete': 'username',
            'class': 'login-input',
        })
        self.fields['username'].label = 'Usuario'
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'placeholder': '••••••••',
            'autocomplete': 'current-password',
            'class': 'login-input',
        })
        self.fields['password'].label = 'Contraseña'


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")
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
        labels = {
            'username': 'Nombre de usuario',
        }
        widgets = {
            'username':   forms.TextInput(),
            'first_name': forms.TextInput(),
            'last_name':  forms.TextInput(),
            'apellido2':  forms.TextInput(),
            'email':      forms.EmailInput(),
            'telefono':   forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget    = forms.PasswordInput()
        self.fields['password1'].label     = 'Contraseña'
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget    = forms.PasswordInput()
        self.fields['password2'].label     = 'Repetir contraseña'
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text  = ''


class UsuarioEditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "apellido2", "email", "telefono", "fecha_nacimiento"]
        labels = {
            "first_name": "Nombre",
            "last_name":  "Primer apellido",
            "apellido2":  "Segundo apellido",
            "email":      "Correo electrónico",
            "telefono":   "Teléfono",
            "fecha_nacimiento": "Fecha de nacimiento",
        }
        widgets = {
            "first_name":       forms.TextInput(),
            "last_name":        forms.TextInput(),
            "apellido2":        forms.TextInput(),
            "email":            forms.EmailInput(),
            "telefono":         forms.TextInput(),
            "fecha_nacimiento": forms.DateInput(attrs={"type": "date"}),
        }