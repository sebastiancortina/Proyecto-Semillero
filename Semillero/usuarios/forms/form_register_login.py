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