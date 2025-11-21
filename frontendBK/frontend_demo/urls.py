from django.urls import path
from django.shortcuts import render

def login_view(request):
    return render(request, "logistica/login.html")

def vehiculos_view(request):
    return render(request, "logistica/vehiculo_list.html")

urlpatterns = [
    # Ruta raíz
    path("", login_view),

    # Login
    path("login", login_view),
    path("login/", login_view),

    # Vehículos
    path("vehiculos", vehiculos_view),
    path("vehiculos/", vehiculos_view),
]
