from django.views.generic import ListView, DetailView
from ..models import Producto

class ListaProductos(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'

class DetalleProducto(DetailView):
    model = Producto
    template_name = 'proyecto_tienda/detalle_producto.html'
    context_object_name = 'producto'
