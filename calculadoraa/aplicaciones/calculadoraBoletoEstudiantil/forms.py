from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['cantidad_bondis', 'cantidad_trenes', 'cantidad_subtes','cantidad_dias']
        