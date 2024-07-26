from django.contrib import admin
from gestionPedidos.models import Servicios, Pedidos, Programador, Clientes
# Register your models here.

admin.site.register(Servicios)
admin.site.register(Pedidos)
admin.site.register(Programador)
admin.site.register(Clientes)