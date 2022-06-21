from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuarios.models import *

class Registraruserlogin(forms.ModelForm):
    class Meta:
       model =  User
       fields = ['nombre_completo', 'email','password',]
       
       labels = {
           'nombre_completo' : '',
           'email' : '' ,
           'password' : ''
       }
       
       # SE PERSONALIZAN LOS CAMPOS DE FORMULARIO
       widgets = {
           'nombre_completo': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'Nombres', 'name':'nombre_completo' } ), 
           'email':  forms.widgets.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"email", 'required':'required', 'placeholder': 'Mail', 'name':'email'}), 
           'password': forms.widgets.TextInput(attrs={ 'class':'form-control form-control-lg','type':"password" , 'required':'required', 'placeholder': 'Password', 'name':'password'})
           }
           
    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
               
        return user
      
    
# class Eliminaradmin(forms.ModelForm):
#     class Meta:
#        model =  Administradores
#        fields = ['cedula']

class RegistrarEstudiante(forms.ModelForm):
    class Meta:
       model =  User
       fields = ['nombre_completo', 'document', 'fecha_n', 'direccion', 'lugar_e', 'lugar_n', 'telefono', 'email' ]
       
       labels = {
           'nombre_completo' : '',
           'document': '',
           'fecha_n': '',
           'direccion': '',
           'lugar_e': '',
           'lugar_n': '',
           'telefono': '',
           'email': '',
       }
       
       # SE PERSONALIZAN LOS CAMPOS DE FORMULARIO
       widgets = {
           'nombre_completo': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'NOMBRE COMPLETO', 'name':'nombre_completo' } ), 
           'document': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'NÚMERO DE IDENTIFICACIÓN', 'name':'document' } ), 
           'fecha_n': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'FECHA DE NACIMIENTO', 'name':'fecha_n' } ), 
           'direccion': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'DIRECCIÓN RESIDENCIA', 'name':'direccion' } ), 
           'lugar_e': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'LUGAR DE EXPEDICIÓN ID', 'name':'lugar_e' } ), 
           'lugar_n': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'LUGAR DE NACIMIENTO', 'name':'lugar_n' } ), 
           'telefono': forms.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"text", 'required':'required', 'placeholder':'TELÉFONO/ CELULAR', 'name':'telefono' } ), 
           'email':  forms.widgets.TextInput(attrs={ 'class':'form-control form-control-lg', 'type':"email", 'required':'required', 'placeholder': 'Mail', 'name':'email'}), 
           }
