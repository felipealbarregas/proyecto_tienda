from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from ..models import Producto

def es_admin(user):
    return user.is_staff

@user_passes_test(es_admin)
def dashboard_administrativo(request):
    productos_bajo_stock = Producto.objects.filter(stock__lte=F('stock_optimo') * 0.9)
    return render(request, 'proyecto_tienda/dashboard_administrativo.html', {'productos': productos_bajo_stock})
