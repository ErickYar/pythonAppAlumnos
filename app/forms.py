from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['codigo','nombre','apellidos','edad','email','carrera']
    
        labels = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'edad':'Edad',
            'email': 'Email',
            'carrera': 'Carrera'
        }

        widgets = {
            'codigo':forms.NumberInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'edad':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'carrera':forms.TextInput(attrs={'class':'form-control'})
        }
