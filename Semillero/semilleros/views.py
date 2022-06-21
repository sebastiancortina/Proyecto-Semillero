from django.shortcuts import render
from .forms.form_register_s import *
from .models import Semilleros
from usuarios.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login-usuarios")
def Solucitud_semillero(request):
    
    template = 'solicitud-semillero.html'
    register_form_semillero = Registrarsemillero()

    if request.method == 'POST':
        register_form_semillero = Registrarsemillero(request.POST)

        if register_form_semillero.is_valid():
           register_form_semillero.save()
            
    return render(request, template, {
        'forms': register_form_semillero
    })



@login_required(login_url="login-usuarios")
def list_semillero_activos(request):
    template = 'list-semillero.html'
    semilleros = Semilleros.objects.filter(is_active=True, is_staff=False)

    return render(request, template, {
         'title': 'Lista de Administradores',
         'listas': semilleros
    })

    #return render(request, template)

def prueba(request):
    return render(request, 'prueba.html',{})

@login_required(login_url="login-usuarios")
def list_semillero_aprobados(request):
    template = 'lista-semillero.html'
    semilleros = Semilleros.objects.filter(is_staff=True)

    return render(request, template, {
         'title': 'Lista de Administradores',
         'listas': semilleros
    })

    #return render(request, template)

def prueba(request):
    return render(request, 'prueba.html',{})