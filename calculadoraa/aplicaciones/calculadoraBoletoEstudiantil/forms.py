from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['cantidad_bondis', 'cantidad_trenes', 'cantidad_subtes','cantidad_dias']
        labels = {
            'cantidad_bondis': 'Cantidad de bondis',
            'cantidad_trenes': 'Cantidad de trenes',
            'cantidad_subtes': 'Cantidad de Subtes',
            'cantidad_dias': 'Cantidad de días'
        }