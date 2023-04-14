import django_filters 
from .models import Alumno

class AlumnoFilter(django_filters.FilterSet):
    
    class Meta:
        model = Alumno
        fields = {
            'dni': ['exact'] 
        }