from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import Cliente, Venta, Producto, VentaAdmin, ProductoAdmin, DetalleVenta
from ventas.forms import ProductoForm, ClienteForm
from django.shortcuts import redirect

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
        return render(request, 'ventas/mainpage.html', {'productos':productos, 'username':request.user.username})

def productos(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        productos = Producto.objects.all()
        return render(request, 'ventas/productos.html', {'productos':productos, 'username':request.user.username})
    
def clientes(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    else:
        clientes = Cliente.objects.all()
        return render(request, 'ventas/clientes.html', {'clientes':clientes, 'username':request.user.username})
    
def producto_nuevo(request):
    if request.POST:
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
        return HttpResponseRedirect("/")
    else:
        form = ProductoForm()
    return render(request, 'ventas/producto_edit.html', {'form':form, 'username':request.user.username})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.POST:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
        return HttpResponseRedirect("/")
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ventas/producto_edit.html', {'form':form, 'username':request.user.username})

def cliente_nuevo(request):
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
        return HttpResponseRedirect("/")
    else:
        form = ClienteForm()
    return render(request, 'ventas/cliente_edit.html', {'form':form, 'username':request.user.username})
    
def cliente_editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.POST:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
        return HttpResponseRedirect("/clientes")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'ventas/cliente_edit.html', {'form':form, 'username':request.user.username})