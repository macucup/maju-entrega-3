from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

def exito(request, nombre, email, telefono):
    return render(request, 'contacto/exito.html', {'nombre': nombre, 'email': email, 'telefono': telefono})

def pagina_principal(request):
    usuarios = User.objects.all()  # Obtener todos los usuarios

    return render(request, 'contacto/contacto.html', {
        'url_login': reverse('login'),
        'url_registro': reverse('registro'),  # Agrega el enlace para el registro de usuario
        'usuarios': usuarios,  # Pasar la lista de usuarios al contexto del template
    })
