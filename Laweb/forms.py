import imp
from tabnanny import verbose
from django import forms
from datetime import date
import datetime

class ClienteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()


class ProductForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    valor=forms.FloatField()
    tipo_producto=forms.CharField(max_length=50)

class PedidoForm(forms.Form):
    objeto=forms.CharField(max_length=50)
    cantidad= forms.IntegerField()
    destino=forms.CharField(max_length=50)
