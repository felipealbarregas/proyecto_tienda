from django.db import models
from django.utils import timezone

class Factura(models.Model):
    pedido = models.OneToOneField('Pedido', on_delete=models.CASCADE, related_name='factura')
    fecha_factura = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.id} para Pedido {self.pedido.id}"
