from django import forms
from django.contrib.auth.forms import AuthenticationForm
from semilleros.models import *

class Registrarsemillero(forms.ModelForm):
    class Meta:
       model =  Semilleros
       fields = ['nombre', 'facultad', 'p_academico', 'g_investigacion', 'l_investigacion', 'tematica_e_i', 'justificacion']
       
       labels = {
           'nombre' : '',
           'facultad': '',
           'p_academico': '', 
           'g_investigacion': '', 
           'l_investigacion': '',
           'tematica_e_i': '', 
           'justificacion': ''
       }

       # SE PERSONALIZAN LOS CAMPOS DE FORMULARIO
       widgets = {
           'nombre': forms.TextInput(attrs={ 'class':'form-control', 'type':"text", 'required':'required', 'placeholder':'NOMBRE DEL SEMILLERO', 'name':'nombre' } ), 
           'facultad':  forms.widgets.TextInput(attrs={ 'class':'form-control', 'type':"text", 'required':'required', 'placeholder': 'FACULTAD', 'name':'facultad'}), 
           'p_academico': forms.widgets.TextInput(attrs={ 'class':'form-control','type':"text" , 'required':'required', 'placeholder': 'PROGRAMA ACADÉMICO', 'name':'p_academico'}),   
           'g_investigacion': forms.widgets.TextInput(attrs={ 'class':'form-control','type':"text" , 'required':'required', 'placeholder': 'GRUPO DE INVESTIGACIÓN AL CUAL ESTÁ VINCULADO EL SEMILLERO', 'name':'g_investigacion'}),   
           'l_investigacion': forms.widgets.TextInput(attrs={ 'class':'form-control','type':"text" , 'required':'required', 'placeholder': 'LÍNEA Y SUBLÍNEA DE INVESTIGACIÓN ASOCIADOS', 'name':'l_investigacion'}),
           'tematica_e_i': forms.widgets.TextInput(attrs={ 'class':'form-control','type':"text" , 'required':'required', 'placeholder': 'TÉMATICA DE ESTUDIO DEL SEMILLERO', 'name':'tematica_e_i'}),
           'justificacion': forms.widgets.TextInput(attrs={ 'class':'form-control','type':"text" , 'required':'required', 'placeholder': 'JUSTIFICACIÓN DEL SEMILLERO DE INVESTIGACIÓN ', 'name':'justificacion'})
        }
      