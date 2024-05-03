from django.views.generic import ListView, DetailView
from ..models import Proveedor

class ListaProveedores(ListView):
    model = Proveedor
    template_name = 'proyecto_tienda/lista_proveedores.html'

class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = 'proyecto_tienda/detalle_proveedor.html'
