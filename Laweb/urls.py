from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('productForm/', prt, name= 'productForm' ),
    path('clienteForm/', clienteForm, name= 'clienteForm' ),
    path('pedidoForm/', pedidos, name='pedidoForm'),
    path('busquedadCliente/', busquedadCliente, name='busquedadCliente'),
    path('busquedadProducto/', busquedadProducto, name='busquedadProducto'),
    path('busquedadPedido/', busquedadPedido, name='busquedadPedido'),
    path('buscar/', buscar, name='buscar'),
    path('',inicio , name= 'inicio'),
   
]