from __future__ import absolute_import,unicode_literals
from django import forms

from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'edad_aproximada',
            'sexo',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]

        labels = {
            'nombre':           'Nombre',
            'edad_aproximada':  'Edad Aproximada',
            'sexo':             'Sexo',
            'fecha_rescate':    'Fecha Rescate',
            'persona':          'Adoptante',
            'vacuna':           'Vacunas',
        }

        widgets = {
            'nombre':               forms.TextInput(attrs={'class':'forms-control'}),
            'edad_aproximada':      forms.TextInput(attrs={'class':'forms-control'}),
            'sexo':                 forms.TextInput(attrs={'class':'forms-control'}),
            'fecha_rescate':        forms.TextInput(attrs={'class':'forms-control'}),
            'persona':              forms.Select(attrs={'class':'forms-control'}),
            'vacuna':               forms.CheckboxSelectMultiple(),
        }