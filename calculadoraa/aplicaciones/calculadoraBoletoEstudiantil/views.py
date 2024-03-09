from django.shortcuts import render
from .models import Estudiante
from .forms import EstudianteForm

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
            precio_subte = 550
            precio_tren = 600
            precio_bondi = 800
            costo_mensual = estudiante.cantidad_bondis * precio_bondi + estudiante.cantidad_subtes * precio_subte + estudiante.cantidad_trenes * precio_tren
            dias_por_mes = estudiante.cantidad_dias*4

            total_bondis_mes = estudiante.cantidad_bondis * precio_bondi * dias_por_mes
            total_subte_mes = estudiante.cantidad_subtes * precio_subte * dias_por_mes
            total_trenes_mes = estudiante.cantidad_trenes * precio_tren * dias_por_mes
            
            estudiante.costo_mensual = costo_mensual*2 * dias_por_mes
            if estudiante.cantidad_dias != 0:
                estudiante.save()
           
            # Guardar en la base de datos si es necesario
            # Esto puede variar dependiendo de tus modelos
            
            return render(request, 'crearEstudiante.html', {'dias':dias_por_mes,'costo_total': estudiante.costo_mensual,'costo_total_bondis':total_bondis_mes,'costo_total_subtes': total_subte_mes , 'costo_total_trenes':total_trenes_mes})
    else:
        form = EstudianteForm()

    return render(request, 'crearEstudiante.html', {'form': form})


# Create your views here.
