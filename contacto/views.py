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

    query = request.GET.get('q', '')  # Obtener el término de búsqueda
    if query:
        productos = Producto.objects.filter(nombre_producto__icontains=query)  # Filtrar productos por el término de búsqueda
    else:
        productos = Producto.objects.all()  # Obtener todos los productos

    # Convertir fechas a cadenas de texto
    productos_list = []
    for producto in productos:
        producto_dict = {
            'id': producto.id,
            'nombre_producto': producto.nombre_producto,
            'precio': producto.precio,
            'ver_mas': producto.ver_mas,
            'fecha': producto.fecha.isoformat(),  # Convertir fecha a cadena de texto
            'imagen_url': producto.imagen.url if producto.imagen else '',
        }
        productos_list.append(producto_dict)

    return render(request, 'contacto/contacto.html', {
        'url_login': reverse('login'),
        'url_registro': reverse('registro'),  # Agrega el enlace para el registro de usuario
        'usuarios': usuarios,  # Pasar la lista de usuarios al contexto del template
        'productos': productos_list,  # Pasar la lista de productos procesados
        'query': query,  # Pasar el término de búsqueda al contexto del template
    })

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  # Pasar request.FILES para manejar archivos
        if form.is_valid():
            form.save()
            return redirect('pagina_principal')
    else:
        form = ProductoForm()
    return render(request, 'contacto/producto_form.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)  # Pasar request.FILES para manejar archivos
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

def ver_mas(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'contacto/ver_mas.html', {'producto': producto})

def sobre_mi(request):
    return render(request, 'contacto/sobre_mi.html')
