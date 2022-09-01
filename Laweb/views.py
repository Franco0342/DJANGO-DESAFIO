from itertools import product
from wsgiref.validate import validator
from django.shortcuts import render
from datetime import date

from .models import Cliente, Pedidos, Producto
from Laweb.forms import ClienteForm, ProductForm, PedidoForm




def inicio(request):
    return render(request, "template/inicio.html")

def clienteForm(request):
    if request.method=="POST":
        form=ClienteForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            phone= info["phone"]
            cliente= Cliente(nombre=nombre, apellido=apellido, email=email, phone=phone)
            cliente.save()
            return render(request, "Laweb/inicio.html", {"mensaje": "Cliente Creado"})
        else:
            return render(request, "Laweb/inicio.html", {"mensaje": "Error"})
    else:
        form=ClienteForm()
        return render(request, "Laweb/clienteForm.html", {'formulario':form})

def prt(request):
    if request.method=="POST":
        miForm=ProductForm(request.POST)
        if miForm.is_valid():
            info= miForm.cleaned_data
            nombre= info["nombre"]
            valor=info["valor"]
            tipo_producto=info["tipo_producto"]

            producto= Producto(nombre=nombre, valor=valor, tipo_producto=tipo_producto)
            producto.save()
            return render(request, "Laweb/inicio.html", {"mensaje": "Producto Creado"})
        else:
            return render(request, "Laweb/inicio.html", {"mensaje": "Error"})
    else:
        miForm=ProductForm()
        return render(request, "Laweb/productForm.html", {'formulario':miForm})

def pedidos(request):
    if request.method=="POST":
        miForm2=PedidoForm(request.POST)
        if miForm2.is_valid():
            info= miForm2.cleaned_data
            objeto=info["objeto"]
            cantidad=info["cantidad"]
            destino=info["destino"]
            pedido=Pedidos(objeto=objeto, cantidad=cantidad, destino=destino)
            pedido.save()
            return render(request, "Laweb/inicio.html", {"mensaje": "Pedido Creado"})
        else:
            return render(request, "Laweb/inicio.html", {"mensaje": "Error"})
    else:
        miForm2=PedidoForm()
        return render(request, "Laweb/pedidoForm.html", {'formulario':miForm2})