from itertools import count
from django.shortcuts import render
from .forms import VueloForm
from .models import Vuelo
from vuelos import models
from django.db.models import Count, Avg, Q

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registrar.html', {'form': form, 'success': True})
    else:
        form = VueloForm()
    return render(request, 'registrar.html', {'form': form})

def listar_vuelos(request):
    vuelos = Vuelo.objects.all().order_by('precio')
    return render(request, 'listar.html', {'vuelos': vuelos})

def estadisticas_vuelos(request):
    estadisticas = Vuelo.objects.aggregate(
        total_vuelos_nacionales = Count('id', filter=Q(tipo='nacional')),
        total_internacionales=Count('id', filter=Q(tipo='internacional')),
        promedio_nacional=Avg('precio', filter=Q(tipo='nacional')),
    )

    return render(request, 'estadisticas.html', {'estadisticas': estadisticas})
