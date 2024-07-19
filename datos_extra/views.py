# datos_extra/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm

@login_required
def user_profile(request):
    # Obtener el perfil del usuario autenticado
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        # Crear instancias de los formularios con los datos del POST
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Guardar los formularios si son válidos
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido modificado con éxito.')
            return redirect('user_profile')
        else:
            # Mensajes de error si hay problemas con los formularios
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        # Crear instancias de los formularios para mostrar en el GET
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'datos_extra/perfil_usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
