from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contacto, Relacion

# Registrar los modelos en el admin
admin.site.register(Contacto)
admin.site.register(Relacion)