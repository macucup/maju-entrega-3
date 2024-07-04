from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Producto
from .forms import ProductoForm

User = get_user_model()

def exito(request, nombre, email, telefono):
    return render(request, 'contacto/exito.html', {'nombre': nombre, 'email': email, 'telefono': telefono})

def pagina_principal(request):
    usuarios = User.objects.all()  # Obtener todos los usuarios
    productos = Producto.objects.all() #Obtener todos productos
    
    return render(request, 'contacto/contacto.html', {
        'url_login': reverse('login'),
        'url_registro': reverse('registro'),  # Agrega el enlace para el registro de usuario
        'usuarios': usuarios,  # Pasar la lista de usuarios al contexto del template
        'productos': productos,
    })


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = ProductoForm()
    return render(request, 'contacto/producto_form.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'contacto/producto_form.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('pagina_principal')
    return render(request, 'contacto/producto_confirm_delete.html', {'producto': producto})

