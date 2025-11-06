from django.db import models

# Create your models here.
from django.db import models

# Modelo para las relaciones (ejemplo: familiar, trabajo, amigo, etc.)
class Relacion(models.Model):
    descripcion = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.descripcion

class Contacto(models.Model):

    nombre = models.CharField(max_length=100, blank=False, null=False)
    
    primer_apellido = models.CharField(max_length=50, blank=False, null=False)
    
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)
    
    alias = models.CharField(max_length=100, blank=True, null=True )
    
    relacion = models.ForeignKey(Relacion, on_delete=models.SET_NULL, null=True)
    
    telefono = models.CharField(max_length=20, unique=True) 
    
    correo = models.EmailField(blank=True, null=True, unique=True)
    
    
    


    def __str__(self):

        return f"{self.nombre} {self.primer_apellido}"