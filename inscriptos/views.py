from django.shortcuts import render
from .models import Alumno
from .filters import AlumnoFilter

def buscarAlumno(request):
   #  lista_alumnos = Alumno.objects.all()
   # alumno_filtrado = ListingFilter(request.GET, queryset=lista_alumnos) 
   # return render(request, 'paginas/inicio.html', {'filtro': alumno_filtrado})
   alumnos = Alumno.objects.all()

   filtro = AlumnoFilter(request.GET, queryset=alumnos)
   alumnos = filtro.qs
   cantidad = alumnos.count()
   get = str(request.method)
   return render(request, 'paginas/inicio.html', {'alumnos': alumnos, 'filtro': filtro, 'cantidad': cantidad, 'get':get} )
