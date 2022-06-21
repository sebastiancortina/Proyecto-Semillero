from django.contrib import admin
from django.urls import path, include
from  .import views

urlpatterns = [
    path('', include('usuarios.urls')),
    path('semillero/prueba', views.prueba, name="prueba"),
    
    #path('semillero/auth/user/login', include('usuarios.urls')),
    path('semillero/solicitud/crear', views.Solucitud_semillero, name="crear-semillero"),
    path('semillero/list', views.list_semillero_activos, name="list-semillero"),
    path('semillero/list/aprobados', views.list_semillero_aprobados, name="list-a-semillero")
    #path('list', views.newUser, name= "list-semillero" )
    
]
