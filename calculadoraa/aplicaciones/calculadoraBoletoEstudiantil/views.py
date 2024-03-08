from django.shortcuts import render
from .models import Estudiante

#Todas las funciones se ejecutan acá
def inicio(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiantes' : estudiantes
    }
    return render(request,'calculadora.html',contexto)
# Create your views here.
