from django.db import models

# Create your models here.
class Clientes (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)  

class Servicios (models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return ' El nombre es: %s y pertenece de la sección es %s . El precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos (models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()

class Programador (models.Model):
    nombre = models.CharField(max_length=30)
    


