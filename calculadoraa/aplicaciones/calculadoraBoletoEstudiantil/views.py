from django.shortcuts import render
from .models import Estudiante
from .forms import EstudianteForm
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

#Todas las funciones se ejecutan acá
def inicio(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiantes' : estudiantes
    }
    return render(request,'base.html',contexto)

def dashboard(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiantes': estudiantes
    }
    return render(request, 'index.html',contexto)

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():

            estudiante = form.save(commit=False)

            precio_subte_diciembre = 80
            precio_tren_diciembre = 30
            precio_bondi_diciembre = 46

            precio_subte = 547
            precio_tren = 600
            precio_bondi = 800

            dias_por_mes = estudiante.cantidad_dias*4
            
            total_bondis_mes_diciembre = estudiante.cantidad_bondis * precio_bondi_diciembre * dias_por_mes * 2
            total_subte_mes_diciembre = estudiante.cantidad_subtes * precio_subte_diciembre * dias_por_mes * 2
            total_trenes_mes_diciembre = estudiante.cantidad_trenes * precio_tren_diciembre * dias_por_mes * 2
            
            estudiante.costo_mensual_diciembre = (total_bondis_mes_diciembre+total_subte_mes_diciembre+ total_trenes_mes_diciembre)

            total_bondis_mes = estudiante.cantidad_bondis * precio_bondi * dias_por_mes * 2
            total_subte_mes = estudiante.cantidad_subtes * precio_subte * dias_por_mes * 2
            total_trenes_mes = estudiante.cantidad_trenes * precio_tren * dias_por_mes * 2
            
            estudiante.costo_mensual = (total_bondis_mes+total_subte_mes+ total_trenes_mes)
            if estudiante.cantidad_dias != 0:
                estudiante.save()
 
            plt.figure(figsize=(7, 4))
            plt.bar(['Diciembre 2023', 'Marzo 2024'], [estudiante.costo_mensual_diciembre,estudiante.costo_mensual])
            plt.xlabel('Mes')
            plt.ylabel('Costo Total (en pesos)')
            plt.title('Comparación del costo total (en pesos) en marzo 2024 y diciembre 2023')
            
            #Esto no tengo ni la más mínima idea de por qué va
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close()


            contexto = {
            'costo_total': estudiante.costo_mensual,
            'costo_diciembre_anterior': estudiante.costo_mensual_diciembre,
            'image_base64': image_base64,
            'dias' : dias_por_mes,
            'costo_total_bondis':total_bondis_mes,
            'costo_total_subtes':total_subte_mes,
            'costo_total_trenes':total_trenes_mes,
        }   

            
            return render(request, 'mostrarResultados.html', contexto)
    else:
        form = EstudianteForm()

    return render(request, 'crearEstudiante.html', {'form': form})

