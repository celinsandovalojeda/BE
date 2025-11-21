from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import (
    Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Ruta, Carga, Despacho
)
from .serializers import (
    VehiculoSerializer, AeronaveSerializer, ConductorSerializer, PilotoSerializer,
    ClienteSerializer, RutaSerializer, CargaSerializer, DespachoSerializer
)

# ==========================
#  VEHICULOS
# ==========================
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["patente", "marca", "modelo"]
    ordering_fields = ["anio", "capacidad_kg"]

    @swagger_auto_schema(
        operation_description="Obtiene la lista de todos los vehículos registrados.",
        tags=["Vehículos"]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Crea un nuevo vehículo.",
        tags=["Vehículos"]
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Obtiene el detalle de un vehículo específico por ID.",
        tags=["Vehículos"]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualiza COMPLETAMENTE un vehículo.",
        tags=["Vehículos"]
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Actualiza PARCIALMENTE un vehículo.",
        tags=["Vehículos"]
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Elimina un vehículo por ID.",
        tags=["Vehículos"]
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# ==========================
#  AERONAVES
# ==========================
class AeronaveViewSet(viewsets.ModelViewSet):
    queryset = Aeronave.objects.all()
    serializer_class = AeronaveSerializer
    permission_classes = [AllowAny]


# ==========================
#  CONDUCTORES  (PROTEGIDO)
# ==========================
class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    permission_classes = [IsAuthenticated]


# ==========================
#  PILOTOS  (PROTEGIDO)
# ==========================
class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.all()
    serializer_class = PilotoSerializer
    permission_classes = [IsAuthenticated]


# ==========================
#  CLIENTES
# ==========================
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]


# ==========================
#  RUTAS
# ==========================
class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer
    permission_classes = [AllowAny]


# ==========================
#  CARGAS
# ==========================
class CargaViewSet(viewsets.ModelViewSet):
    queryset = Carga.objects.all()
    serializer_class = CargaSerializer
    permission_classes = [AllowAny]


#  DESPACHOS 

class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer
    permission_classes = [IsAuthenticated]
