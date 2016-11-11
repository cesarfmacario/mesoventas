from django.db import models
from django.contrib import admin
from django.utils import timezone

class Producto(models.Model):    
    #id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencias = models.IntegerField(default=0)
    #imagen = models.ImageField(upload_to='static/imagenes/', default='static/imagenes/noimg.jpg')
    
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    #id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    direccion = models.CharField(max_length=250)
        
    def __str__(self):
        return self.nombre    

class Venta(models.Model):    
    numfactura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateTimeField(default=timezone.now)
    productos = models.ManyToManyField(Producto, through='DetalleVenta')
    total = models.FloatField(default=0)
    
    def __str__(self):
        return self.numfactura

class DetalleVenta(models.Model):        
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadvendida = models.IntegerField(default = 0)
    totaldetalle = models.FloatField(default=0)
    
class DetalleVentaInLine(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class ProductoAdmin(admin.ModelAdmin):
    inlines = (DetalleVentaInLine,)

class VentaAdmin(admin.ModelAdmin):
    inlines = (DetalleVentaInLine,)
