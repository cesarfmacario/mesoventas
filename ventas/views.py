from django.shortcuts import render
from .models import Cliente, Venta, Producto, VentaAdmin, ProductoAdmin, DetalleVenta
# Create your views here.

def login(request):
    return render(request, 'ventas/login.html', {})

def mainpage(request):
    productos = Producto.objects.all()#order_by('precio')
    return render(request, 'ventas/mainpage.html', {'productos': productos})


