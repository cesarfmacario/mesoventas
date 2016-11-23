from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from ventas.models import Cliente, Venta, Producto, VentaAdmin, ProductoAdmin, DetalleVenta
from ventas.forms import ProductoForm, ClienteForm, VentaForm
from django.shortcuts import redirect
from django.utils import timezone

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
        #return HttpResponse('<script>alert("Holi")</script>')
    else:
        username = password = ''
        if request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/login")
        return render(request, "ventas/login.html", {})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        username = password = email = ''
        if request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if(username != '' and email != '' and password != ''):
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/signup")
        return render(request, "ventas/signup.html", {})
    
def mainpage(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login")
    else:
        productos = Producto.objects.all()
        return render(request, 'ventas/mainpage.html', {'productos':productos, 'username':request.user})

def productos(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        productos = Producto.objects.all()
        return render(request, 'ventas/productos.html', {'productos':productos, 'username':request.user})
    
def clientes(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        clientes = Cliente.objects.all()
        return render(request, 'ventas/clientes.html', {'clientes':clientes, 'username':request.user})

def ventas(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        #ventas = Venta.objects.all()
        ventas = Venta.objects.order_by('-numfactura')
        return render(request, 'ventas/ventas.html', {'ventas':ventas, 'username':request.user})

def producto_nuevo(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.POST:
            form = ProductoForm(request.POST)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.save()
            return HttpResponseRedirect("/productos")
        else:
            form = ProductoForm()
        return render(request, 'ventas/producto_edit.html', {'form':form, 'username':request.user})

def producto_editar(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        producto = get_object_or_404(Producto, pk=pk)
        if request.POST:
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.save()
            return HttpResponseRedirect("/productos")
        else:
            form = ProductoForm(instance=producto)
        return render(request, 'ventas/producto_edit.html', {'form':form, 'username':request.user})

def cliente_nuevo(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.POST:
            form = ClienteForm(request.POST)
            if form.is_valid():
                cliente = form.save(commit=False)
                cliente.save()
            return HttpResponseRedirect("/clientes")
        else:
            form = ClienteForm()
        return render(request, 'ventas/cliente_edit.html', {'form':form, 'username':request.user})
    
def cliente_editar(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        cliente = get_object_or_404(Cliente, pk=pk)
        if request.POST:
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                cliente = form.save(commit=False)
                cliente.save()
            return HttpResponseRedirect("/clientes")
        else:
            form = ClienteForm(instance=cliente)
        return render(request, 'ventas/cliente_edit.html', {'form':form, 'username':request.user})
    
def ventas_nuevo(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.POST:
            form = VentaForm(request.POST)
            if form.is_valid():
                #cl = 
                ventanueva = Venta.objects.create(cliente=form.cleaned_data['cliente'], usuario=request.user)
                
                total = 0
                for producto_id in request.POST.getlist('productos'):
                    prodselect = Producto.objects.filter(id=int(producto_id))[0]
                    prodselect
                    exists = prodselect.existencias
                    prodselect.existencias = exists - 1
                    prodselect.save()
                    totdet = prodselect.precio
                    total = total + totdet
                    detalle = DetalleVenta(venta_id=ventanueva.numfactura, producto_id=producto_id, totaldetalle=totdet)
                    detalle.save()
                
                ventanueva.total = total
                ventanueva.save()
                
            return HttpResponseRedirect("/ventas")
        else:
            form = VentaForm()
            ventas = Venta.objects.all()
            ventas = Venta.objects.all()[len(ventas) - 1]
            numfact = ventas.numfactura + 1
            return render(request, 'ventas/ventas_nuevo.html', {'form':form, 'fecha':timezone.now, 'numfact':numfact, 'username':request.user})

def ventas_nuev(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        if request.POST:
            return HttpResponse("post recibido")
        else:
            clientes = Cliente.objects.all()
            productos = Producto.objects.all()
            ventas = Venta.objects.all()
            numfact = len(ventas) + 1
            fecha = timezone.now
            info =  {'clientes':clientes,'productos':productos, 'fecha':fecha, 'numfact':numfact, 'username':request.user, 'prods':prods, 'cantvend':cantvend}
            return render(request, 'ventas/ventanueva.html', info)
    
def ventas_detalle(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        venta = get_object_or_404(Venta, pk=pk)
        detalles = DetalleVenta.objects.filter(venta=venta)
        prunits = []   #   PRECIOS UNITARIOS DEBIDO A QUE UNA ACTUALIZACION DE PRODUCTOS AFECTARÍA ESTE CAMPO
        for x in range(0, len(detalles)):
            prunits.append(detalles[x].totaldetalle / detalles[x].cantidadvendida)
        longdetalles = len(detalles)
        info = {'venta':venta, 'detalles':detalles, 'username':request.user, 'prunits':prunits, 'longdet':longdetalles}
        return render(request, 'ventas/ventas_detalle.html', info)

def producto_eliminar(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return HttpResponseRedirect("/productos")
    
def cliente_eliminar(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        return HttpResponseRedirect("/clientes")
    