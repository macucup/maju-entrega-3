from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'datos_extra/perfil_usuario.html', {'user_profile': user_profile, 'form': form})
