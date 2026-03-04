from django.db import models

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    matricula = models.CharField(max_length=15, unique=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.matricula})"

class Reserva(models.Model):
    # Aquí está la relación entre las dos entidades
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Reserva de {self.nombre_cliente} - {self.vehiculo.matricula}"

