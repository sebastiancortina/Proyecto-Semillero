from django.db import models
from usuarios.models import User

# Create your models here.
class Semilleros(models.Model):
    nombre = models.CharField(max_length=250)
    facultad = models.CharField(max_length=250)
    p_academico = models.CharField(max_length=250)
    g_investigacion = models.CharField(max_length=250)
    l_investigacion = models.CharField(max_length=250)
    tematica_e_i = models.CharField(max_length=250)
    justificacion = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Semilleros'