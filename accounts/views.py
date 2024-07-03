# En accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class RegistroUsuario(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registro.html'

class CustomLogoutView(LogoutView):
    next_page = 'pagina_principal'
