from django.contrib import admin
from .models import Cliente, Venta, Producto, VentaAdmin, ProductoAdmin

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)

