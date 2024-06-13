from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactoForm
import logging  # Importa logging si prefieres usarlo para depuración

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()

            # Depuración adicional con print()
            print(f'Nombre: {contacto.nombre}')
            print(f'Email: {contacto.email}')
            print(f'Teléfono: {contacto.telefono}')

            # Redirigir a la vista exito con los datos del contacto
            return redirect(reverse('exito', kwargs={'nombre': contacto.nombre, 'email': contacto.email, 'telefono': contacto.telefono}))
    else:
        form = ContactoForm()
    
    return render(request, 'contacto.html', {'form': form})

def exito(request, nombre, email, telefono):
    return render(request, 'exito.html', {'nombre': nombre, 'email': email, 'telefono': telefono})
