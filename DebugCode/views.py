from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {})

def searchingServices(request):
    return render(request, 'searching.html', {})

def search(request):
    mensaje = f'Servicio buscado: {request.GET.get("ss", "")}'
    return HttpResponse(mensaje)
