from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contacto, Relacion

def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'listar.html', {'contactos': contactos})

from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contacto, Relacion

from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contacto, Relacion

def crear_contacto(request):
    if request.method == 'POST':
        # Convertir texto a mayúsculas
        nombre = request.POST['nombre'].upper()
        primer_apellido = request.POST['primer_apellido'].upper()
        segundo_apellido = request.POST.get('segundo_apellido', '').upper()
        alias = request.POST.get('alias', '').upper()
        telefono = request.POST['telefono']
        correo = request.POST.get('correo', '').strip().lower()
        relacion_id = request.POST['relacion']

        # Verificar duplicados
        if Contacto.objects.filter(telefono=telefono).exists():
            messages.error(request, f"Ya existe un contacto con el teléfono {telefono}.")
        elif correo and Contacto.objects.filter(correo=correo).exists():
            messages.error(request, f"Ya existe un contacto con el correo {correo}.")
        else:
            try:
                relacion = Relacion.objects.get(id=relacion_id)
                Contacto.objects.create(
                    nombre=nombre,
                    primer_apellido=primer_apellido,
                    segundo_apellido=segundo_apellido,
                    alias=alias,
                    relacion=relacion,
                    telefono=telefono,
                    correo=correo if correo else None
                )
                messages.success(request, "Contacto creado exitosamente.")
                return redirect('listar')
            except IntegrityError:
                messages.error(request, "Error al crear el contacto.")

    relaciones = Relacion.objects.all()
    return render(request, 'crear.html', {'relaciones': relaciones})



def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.nombre = request.POST['nombre'].upper()
        contacto.primer_apellido = request.POST['primer_apellido'].upper()
        contacto.segundo_apellido = request.POST.get('segundo_apellido', '').upper()
        contacto.alias = request.POST.get('alias', '').upper()
        contacto.telefono = request.POST['telefono']
        contacto.correo = request.POST.get('correo', '').lower()
        relacion_id = request.POST['relacion']
        contacto.relacion = Relacion.objects.get(id=relacion_id)
        contacto.save()
        messages.success(request, "✅ Contacto actualizado correctamente.")
        return redirect('listar')

    relaciones = Relacion.objects.all()
    return render(request, 'editar.html', {'contacto': contacto, 'relaciones': relaciones})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    messages.success(request, "🗑️ Contacto eliminado correctamente.")
    return redirect('listar')