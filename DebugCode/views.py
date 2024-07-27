from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Servicios

from django.core.mail import send_mail
from django.conf import settings

from DebugCode.forms import ContactForm

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
        subject = request.POST['asunto']
        email = request.POST['email']     
        message = request.POST['mensaje'] + " | Enviado por: " + email
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['maria.victoria.webdev@gmail.com']

        send_mail(subject, message, email_from, recipient_list)

        return render (request, 'gracias.html')
    
    return render(request, 'contact.html', {})

def contactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            infForm = form.cleaned_data
            send_mail(
                infForm['subject'],
                infForm['message'],
                infForm.get('email', ''),
                ['maria.victoria.webdev@gmail.com']
            )
            return render(request, 'home.html')
    else:
        form = ContactForm()
    
    return render(request, 'contactForm.html', {'form': form})