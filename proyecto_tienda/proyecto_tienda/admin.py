# gestion/admin.py
from django.contrib import admin
from .models import Producto, Proveedor, Cliente, Pedido, Factura

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'necesita_restock')
    list_filter = ('proveedor', 'stock')
    actions = ['reordenar_stock']

    def necesita_restock(self, obj):
        return obj.stock <= obj.stock_optimo * 0.9
    necesita_restock.boolean = True

    def reordenar_stock(self, request, queryset):
        # Implementar lógica para reordenar o enviar alertas
        pass
    reordenar_stock.short_description = 'Reordenar stock seleccionado'

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Factura)
