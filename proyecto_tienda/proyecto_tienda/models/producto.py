# gestion/models/producto.py
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    stock_optimo = models.IntegerField(default=100)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True, related_name='productos')

    def necesita_restock(self):
        return self.stock <= self.stock_optimo * 0.9
