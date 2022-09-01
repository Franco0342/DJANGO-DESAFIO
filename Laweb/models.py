from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    valor=models.FloatField()
    tipo_producto=models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    def __str__(self):
        return self.nombre+""+str(self.apellido)

class Pedidos(models.Model):
    objeto=models.CharField(max_length=50)
    cantidad= models.IntegerField()
    destino=models.CharField(max_length=50)
    def __str__(self):
        return self.objeto
