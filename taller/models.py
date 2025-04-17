from django.db import models

# Create your models here.
class Auto(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    propietario = models.CharField(max_length=100)
    marca = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.patente} - {self.propietario}"


class Reparacion(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='reparaciones')
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reparación de {self.auto.patente} - {self.fecha}"