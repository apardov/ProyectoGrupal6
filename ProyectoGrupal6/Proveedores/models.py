from django.db import models
from django.contrib.auth.models import Group


# Create your models here.

class Proveedores(models.Model):
    rut_proveedor = models.CharField(max_length=100)
    nombre_proveedor = models.CharField(max_length=100)
    nombre_representante = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name_plural = 'Proveedores'
        verbose_name = 'Proveedor'
