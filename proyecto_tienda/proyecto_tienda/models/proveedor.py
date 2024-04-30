# gestion/models/proveedor.py
from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    cif = models.CharField(max_length=15)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    iva = models.DecimalField(max_digits=4, decimal_places=2, default=21.0)

    def __str__(self):
        return self.nombre
