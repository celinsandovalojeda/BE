from django.db import models

# ======================================
# CHOICES
# ======================================
TIPO_TRANSPORTE_CHOICES = [
    ('TERRESTRE', 'Transporte Terrestre'),
    ('AEREO', 'Transporte Aéreo'),
]

ESTADO_DESPACHO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('EN_RUTA', 'En ruta'),
    ('ENTREGADO', 'Entregado'),
]


# ======================================
# MODELOS
# ======================================

class Vehiculo(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    capacidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(
        max_length=20,
        choices=[('CAMION', 'Camión'), ('FURGON', 'Furgón'), ('BUS', 'Bus')]
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patente} - {self.marca} {self.modelo}"


class Aeronave(models.Model):
    matricula = models.CharField(max_length=15, unique=True)
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.PositiveIntegerField()
    capacidad_kg = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(
        max_length=20,
        choices=[('AVION', 'Avión'), ('HELICOPTERO', 'Helicóptero')]
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.matricula} - {self.modelo}"


class Conductor(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    licencia = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Piloto(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    certificacion = models.CharField(max_length=50)
    horas_vuelo = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Ruta(models.Model):
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tipo_transporte = models.CharField(
        max_length=20,
        choices=TIPO_TRANSPORTE_CHOICES
    )
    distancia_km = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    duracion_estimada_horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.origen} → {self.destino} ({self.tipo_transporte})"
