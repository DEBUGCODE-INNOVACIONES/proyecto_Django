from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombres y Apellidos')
    direccion = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=10, verbose_name='Teléfono/Celular') 

    def __str__(self):
        return self.nombre 

class Servicios (models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.seccion

class Pedidos (models.Model):
    nombre= models.CharField(max_length=30, null=True, blank=True)
    fecha = models.DateField()
    entregado = models.BooleanField()
    enProceso=models.BooleanField(null=True, blank=True)
    verificando=models.BooleanField(null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.entregado)

class Programador (models.Model):
    nombre = models.CharField(max_length=30)
    desarrollo= models.CharField(max_length=30, null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre
    


