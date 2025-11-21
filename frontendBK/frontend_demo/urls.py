from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from transporte.views import VehiculoViewSet
from django.shortcuts import render

# Router
router = DefaultRouter()
router.register(r"vehiculos", VehiculoViewSet, basename="vehiculos")

# Vistas frontend
def login_view(request):
    return render(request, "logistica/login.html")

def vehiculos_view(request):
    return render(request, "logistica/vehiculo_list.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login_view),
    path("vehiculos/", vehiculos_view),
    path("api/", include(router.urls)),
]
