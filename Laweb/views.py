from itertools import product
from wsgiref.validate import validator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente, Pedidos, Producto
from Laweb.forms import ClienteForm, ProductForm, PedidoForm





def inicio(request):
    return render(request, "Laweb/inicio.html")

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


def busquedadCliente(request):
    return render(request, "Laweb/busquedadCliente.html")

def buscar(request):
    apellido=request.POST.get("apellido")
    clientes=Cliente.objects.filter(apellido=apellido)
    return render(request, "Laweb/resultadoBusquedad.html", {"clientes":clientes})

def busquedadProducto(request):
    return render(request, "Laweb/busquedadProducto.html")

def buscar(request):
    tipo_producto=request.POST.get("tipo_producto")
    productos=Producto.objects.filter(tipo_producto=tipo_producto)
    return render(request, "Laweb/resultadoBusquedad1.html", {"productos":productos})


def busquedadPedido(request):
    return render(request, "Laweb/busquedadPedido.html")

def buscar(request):
    destino=request.POST.get("destino")
    pedidos=Pedidos.objects.filter(destino=destino)
    return render(request, "Laweb/resultadoBusquedad2.html", {"pedidos":pedidos})



    
        


