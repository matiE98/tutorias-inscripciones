from django.db import models

class Alumno(models.Model):
    dni = models.IntegerField(primary_key=True)
    apellido = models.TextField(max_length=250, null=False, default='-')
    nombre = models.TextField(max_length=250, null=False, default='-')
    carrera = models.CharField(max_length=30, null=False, default='-')
    email = models.CharField(max_length= 100, null=False, default='-')
    def __str__(self):
        return self.dni