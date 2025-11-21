from rest_framework import serializers
from .models import (
    Vehiculo, Aeronave, Conductor, Piloto,
    Cliente, Ruta, Carga, Despacho
)

# =========================
# VEHICULOS
# =========================
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


# =========================
# AERONAVES
# =========================
class AeronaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aeronave
        fields = '__all__'


# =========================
# CONDUCTORES
# =========================
class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'


# =========================
# PILOTOS
# =========================
class PilotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piloto
        fields = '__all__'


# =========================
# CLIENTES
# =========================
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


# =========================
# RUTAS
# =========================
class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'


# =========================
# CARGAS
# =========================
class CargaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(),
        source='cliente',
        write_only=True
    )

    class Meta:
        model = Carga
        fields = [
            'id', 'descripcion', 'peso_kg', 'tipo',
            'valor_declarado', 'cliente', 'cliente_id'
        ]


# =========================
# DESPACHOS
# =========================
class DespachoSerializer(serializers.ModelSerializer):
    ruta = RutaSerializer(read_only=True)
    ruta_id = serializers.PrimaryKeyRelatedField(
        queryset=Ruta.objects.all(),
        source='ruta',
        write_only=True
    )

    vehiculo = VehiculoSerializer(read_only=True)
    vehiculo_id = serializers.PrimaryKeyRelatedField(
        queryset=Vehiculo.objects.all(),
        source='vehiculo',
        write_only=True,
        allow_null=True
    )

    aeronave = AeronaveSerializer(read_only=True)
    aeronave_id = serializers.PrimaryKeyRelatedField(
        queryset=Aeronave.objects.all(),
        source='aeronave',
        write_only=True,
        allow_null=True
    )

    conductor = ConductorSerial
