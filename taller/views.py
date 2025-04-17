from django.shortcuts import render,redirect,get_object_or_404
from .models import Auto, Reparacion
from .forms import AutoForm, ReparacionForm

# Create your views here.


def homepage(request):
    return render(request, 'paginaprincipal.html')


def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'lista_autos.html', {'autos': autos})

def historial_reparaciones(request, patente):
    auto = get_object_or_404(Auto, patente=patente)
    reparaciones = auto.reparaciones.all()
    return render(request, 'historial_reparaciones.html', {'auto': auto, 'reparaciones': reparaciones})

def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autos')
    else:
        form = AutoForm()
    return render(request, 'formulario_auto.html', {'form': form})

def crear_reparacion(request, patente):
    auto = get_object_or_404(Auto, patente=patente)  # Busca el auto por su patente
    if request.method == 'POST':
        form = ReparacionForm(request.POST)
        if form.is_valid():
            reparacion = form.save(commit=False)
            reparacion.auto = auto  # Asocia la reparación al auto
            reparacion.save()
            return redirect('lista_autos')  # Cambia según la URL donde quieras redirigir
    else:
        form = ReparacionForm()
    return render(request, 'formulario_reparaciones.html', {'form': form, 'auto': auto})