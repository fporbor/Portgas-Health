from django import forms
from .models import Ejercicio


class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = ['nombre', 'tipo_ejercicio', 'grupo_muscular', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del ejercicio'
            }),
            'tipo_ejercicio': forms.Select(attrs={
                'class': 'form-select'
            }),
            'grupo_muscular': forms.CheckboxSelectMultiple(),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del ejercicio...'
            }),
        }