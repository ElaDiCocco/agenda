from django.shortcuts import render
from .models import Contacto
# Create your views here.
def contacto_index(request):
    contacts = Contacto.objects.all()
    return render(request, 'contactos/index.html', {'contactos': contacts})
