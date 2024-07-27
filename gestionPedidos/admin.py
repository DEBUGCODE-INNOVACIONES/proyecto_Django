from django.contrib import admin
from gestionPedidos.models import Servicios, Pedidos, Programador, Clientes
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email',)
    search_fields = ('nombre', 'email',)
    list_filter = ('nombre',)
    

class ServiciosAdmin(admin.ModelAdmin):
    list_filter = ('seccion',)
    search_fields = ('nombre', )

class ProgrammerAdmin(admin.ModelAdmin):
    list_filter = ('nombre',)
    search_fields = ('nombre', 'desarrollo')

 

class PedidosAdmin(admin.ModelAdmin):
    list_display = ('nombre','id')
    list_filter = ('entregado', 'fecha',)
    search_fields = ('nombre', )
    date_hierarchy='fecha'

admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
admin.site.register(Programador, ProgrammerAdmin)
admin.site.register(Clientes, ClientesAdmin)