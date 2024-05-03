from django.views.generic import ListView, DetailView
from ..models import Cliente

class ListaClientes(ListView):
    model = Cliente
    template_name = 'proyecto_tienda/lista_clientes.html'

class DetalleCliente(DetailView):
    model = Cliente
    template_name = 'proyecto_tienda/detalle_cliente.html'
