from django.urls import path
from . import views

urlpatterns = [
    path('autos/', views.lista_autos, name='lista_autos'),
    path('autos/nuevo/', views.crear_auto, name='crear_auto'),
    path('autos/<str:patente>/', views.historial_reparaciones, name='historial_reparaciones'),
    path('reparaciones/nueva/<str:patente>/', views.crear_reparacion, name='crear_reparacion'),
]
