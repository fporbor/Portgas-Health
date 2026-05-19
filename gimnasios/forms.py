from django import forms
from .models import Gimnasio

class GimnasioForm(forms.ModelForm):
    class Meta:
        model = Gimnasio
        fields = '__all__'
        widgets = {
            'nombre':    forms.TextInput(),
            'telefono':  forms.TextInput(),
            'email':     forms.EmailInput(),
            'provincia': forms.TextInput(),
            'localidad': forms.TextInput(),
            'direccion': forms.TextInput(),
        }
