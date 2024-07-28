from django.http import HttpResponse
from django.shortcuts import render
import datetime

# First view function
def fecha(request):
    fecha_actual = datetime.datetime.now()
    return HttpResponse(f"<h1>{fecha_actual}</h1>")

# Home view function
def home(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "home.html", {'fecha': fecha_actual})

def portfolio(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "portfolio.html", {'fecha': fecha_actual})