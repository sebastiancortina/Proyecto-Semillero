from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# class UserManager(BaseUserManager):

#     def create_user(self, email, password=None, **extra_fields):
#         """Creates and saves a new user"""
#         if not email:
#             raise ValueError('This object requires an email')
            
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, password):
#         user = self.create_user(email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

#         return user

class  UserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico !')
        
        user = self.model(email = self.normalize_email(email), **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password = None, **extra_fields):

        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    nombre_completo = models.CharField(max_length=255, blank=True, null=True)
    document = models.CharField(max_length=255, unique=True, blank=True, null=True)
    fecha_n = models.CharField(max_length=255, blank=True, null=True)
    direccion = models.CharField(max_length=255, unique=True, blank=True, null=True)
    lugar_e = models.CharField(max_length=255,  blank=True, null=True)
    lugar_n = models.CharField(max_length=255,  blank=True, null=True)
    telefono = models.CharField(max_length=255, unique=True, blank=True, null=True )
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField( max_length=254 )
    emergencia_n = models.CharField(max_length=255, blank=True, null=True)
    emergencia_c = models.CharField(max_length=255,  blank=True, null=True)
    rol = models.CharField(max_length=255, blank=True, null=True, default='estudiante')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    create_at = models.DateTimeField(auto_now_add=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'

    EQUIRED_FIELDS = []

    def __str__(self):
        return f"usurario  {self.nombre_completo} {self.email} {self.rol} "

    class Meta:
        db_table = 'User'