from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import Cliente, Venta, Producto, VentaAdmin, ProductoAdmin, DetalleVenta

productos = Producto.objects.all()

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
        usr = request.user.username
        return render(request, 'ventas/mainpage.html', {'productos':productos, 'username':usr})
