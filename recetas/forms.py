from django import forms
from .models import Receta


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['nombre', 'proteina', 'calorias', 'objetivo', 'alergia', 'descripcion', 'video_url']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la receta'
            }),
            'proteina': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Proteína (g)'
            }),
            'calorias': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Calorías (kcal)'
            }),
            'objetivo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'alergia': forms.CheckboxSelectMultiple(),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción de la receta...'
            }),
            'video_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL del video de YouTube (opcional)'
            }),
        }