from django.views.generic import ListView, DetailView
from ..models import Pedido

class ListaPedidos(ListView):
    model = Pedido
    template_name = 'proyecto_tienda/lista_pedidos.html'

class DetallePedido(DetailView):
    model = Pedido
    template_name = 'proyecto_tienda/detalle_pedido.html'