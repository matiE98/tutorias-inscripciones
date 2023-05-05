from django.db import models

class Alumno(models.Model):
    dni = models.IntegerField(primary_key=True)
    apellido = models.CharField(max_length=250, null=False, default='sin_apellido')
    nombre = models.CharField(max_length=250, null=False, default='sin_nombre')
    carrera = models.CharField(max_length=30, null=False, default='sin_carrera')

    def __str__(self):
        return self.dni