from django import forms
from django.contrib.auth.models import User
from ventas.models import Producto, Cliente
from django.forms import ModelForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio','existencias',)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre', 'nit','direccion',)

def __init__ (self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields["actores"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["actores"].help_text = "Ingrese los Actores que participaron en la película"
        self.fields["actores"].queryset = Actor.objects.all()
