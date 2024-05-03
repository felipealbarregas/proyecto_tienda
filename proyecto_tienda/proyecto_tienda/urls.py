from django.urls import path
from django.contrib import admin
from .views import (
    ListaProductos, DetalleProducto,
    ListaProveedores, DetalleProveedor,
    ListaClientes, DetalleCliente,
    ListaPedidos, DetallePedido,
    dashboard_administrativo
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', ListaProductos.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', DetalleProducto.as_view(), name='detalle_producto'),
    path('proveedores/', ListaProveedores.as_view(), name='lista_proveedores'),
    path('proveedores/<int:pk>/', DetalleProveedor.as_view(), name='detalle_proveedor'),
    path('clientes/', ListaClientes.as_view(), name='lista_clientes'),
    path('clientes/<int:pk>/', DetalleCliente.as_view(), name='detalle_cliente'),
    path('pedidos/', ListaPedidos.as_view(), name='lista_pedidos'),
    path('pedidos/<int:pk>/', DetallePedido.as_view(), name='detalle_pedido'),
    path('admin/dashboard/', dashboard_administrativo, name='dashboard_administrativo'),
]
