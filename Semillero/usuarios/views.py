
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
from .forms.form_register_login import *

def loginsesion(request):

    if request.method == 'POST':
        username = request.POST.get('ususario')
        password = request.POST.get('contrasena')
        
        user = authenticate(request, email = username, password = password)
        
        if user is not None:
            login(request, user)
            # return render(request, 'index-admin.html', { 
            #     'email': username
            # })
            return redirect('index-admin')
        else:
            pass


    return render(request, 'login.html')

def cerrarsesion(request):
   logout(request) 
   return redirect('login-usuarios')

@login_required(login_url="login-usuarios")
def index(request):
    return render(request,'index-admin.html')

def newUser(request):
    template = 'registrar.html'
    register_form_user_login = Registraruserlogin()

    if request.method == 'POST':
        register_form_user_login = Registraruserlogin(request.POST)
        if  register_form_user_login.is_valid():
            register_form_user_login.save()
            return redirect('login-usuarios')
        else:
            pass
            #messages.success(request, 'administrador ya registrado !!')


        #return render(request, template)
    
    return render(request, template, {
        'form_logins': register_form_user_login
    })


            