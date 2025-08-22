from django.urls import path
from . import views

app_name = 'vuelos'

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_vuelo, name='registrar'),
    path('listar/', views.listar_vuelos, name='listar'),
    path('estadisticas/', views.estadisticas_vuelos, name='estadisticas'),
]