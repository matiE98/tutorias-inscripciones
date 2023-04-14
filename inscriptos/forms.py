from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'carrera']
