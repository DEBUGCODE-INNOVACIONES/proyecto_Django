from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Servicios

def home(request):
    return render(request, 'home.html', {})

def searchingServices(request):
    return render(request, 'searching.html', {})


def search(request):
    serv = request.GET.get('ss', '')

    if serv:
        if len(serv) > 15:
            mensaje = 'Búsqueda demasiado extensa. Por favor, ingrese una búsqueda más corta.'
            return HttpResponse(mensaje)
        else:
            servicios = Servicios.objects.filter(seccion__icontains=serv)
            return render(request, 'encontrados.html', {'servicios': servicios, 'query': serv})
    else:
        mensaje = 'No se encontró el Servicio'
        return HttpResponse(mensaje)

def contact(request):
    if request.method == 'POST':
        return render (request, 'gracias.html')
    return render(request, 'contact.html', {})