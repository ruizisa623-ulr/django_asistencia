from django import forms
from .models import Asistencia

class Asistencia(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['tipo_documento', 'documento', 'nombre', 'apellido', 'whatsapp', 'fecha', 'asistio']
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'asistio': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }