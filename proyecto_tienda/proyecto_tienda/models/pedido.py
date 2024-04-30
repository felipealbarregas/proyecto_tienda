from django.db import models
from django.utils import timezone

class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(default=timezone.now)
    entregado = models.BooleanField(default=False)
    detalles = models.TextField(blank=True, null=True)  # Optional field for additional details

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"
