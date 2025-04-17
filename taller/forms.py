from django import forms
from .models import Auto, Reparacion

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['patente', 'propietario', 'marca', 'modelo']

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = ['auto', 'descripcion', 'costo']
