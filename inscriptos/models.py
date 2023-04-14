from django.db import models

class Alumno(models.Model):
    dni = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=250, null=False, default='sin_nombre')
    carrera = models.CharField(max_length=5, null=False, default='sin_carrera')

    def __str__(self):
        return self.dni