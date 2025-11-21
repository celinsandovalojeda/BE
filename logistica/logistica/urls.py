from django.urls import path, include
from rest_framework.routers import DefaultRouter

# API: ViewSets del backend de tu compañera
from .views import (
    VehiculoViewSet, AeronaveViewSet, ConductorViewSet, PilotoViewSet,
    ClienteViewSet, RutaViewSet, CargaViewSet, DespachoViewSet
)

# FRONTEND: tus vistas con templates
from . import views_frontend


# =========================
# ROUTER PARA LA API REST
# =========================
router = DefaultRouter()
router.register(r"vehiculos", VehiculoViewSet)
router.register(r"aeronaves", AeronaveViewSet)
router.register(r"conductores", ConductorViewSet)
router.register(r"pilotos", PilotoViewSet)
router.register(r"clientes", ClienteViewSet)
router.register(r"rutas", RutaViewSet)
router.register(r"cargas", CargaViewSet)
router.register(r"despachos", DespachoViewSet)


# =========================
# URLS DE FRONTEND (TEMPLATES HTML)
# =========================
urlpatterns = [

    # --- VEHÍCULOS ---
    path("vehiculos/", views_frontend.vehiculo_list, name="vehiculo_list"),
    path("vehiculos/crear/", views_frontend.vehiculo_create, name="vehiculo_create"),
    path("vehiculos/editar/<int:id>/", views_frontend.vehiculo_edit, name="vehiculo_edit"),
    path("vehiculos/eliminar/<int:id>/", views_frontend.vehiculo_delete, name="vehiculo_delete"),

    # --- AERONAVES ---
    path("aeronaves/", views_frontend.aeronave_list, name="aeronave_list"),
    path("aeronaves/crear/", views_frontend.aeronave_create, name="aeronave_create"),
    path("aeronaves/editar/<int:id>/", views_frontend.aeronave_edit, name="aeronave_edit"),
    path("aeronaves/eliminar/<int:id>/", views_frontend.aeronave_delete, name="aeronave_delete"),

    # (Luego agregamos los otros CRUDs si quieres)

    # API REST completa
    path("api/", include(router.urls)),
]