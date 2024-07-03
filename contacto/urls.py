from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import RegistroUsuario  

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('exito/<str:nombre>/<str:email>/<str:telefono>/', views.exito, name='exito'),
    path('accounts/registro/', RegistroUsuario.as_view(), name='registro'),  # Ruta para la vista de registro
    # Otras URLs específicas de contacto
]
