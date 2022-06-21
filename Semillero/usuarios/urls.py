from django.contrib import admin
from django.urls import path, include
from  . import views

urlpatterns = [
    path('', views.loginsesion, name= "login-usuarios"),
    path('logout', views.cerrarsesion, name= "logout-usuarios"),

    path('user/index/admin', views.index, name= "index-admin"),
    path('registrar', views.newUser, name= "registrar-usuarios"),
    path('registrar/estudiante', views.newEstudiante, name= "registrar-estudiante"),
   # path('registrar', views.newUser, name= "registrar-usuarios"),




    #path('list', views.newUser, name= "list-semillero" )
    
]
