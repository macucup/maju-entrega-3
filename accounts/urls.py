from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegistroUsuario, CustomLogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # URL para iniciar sesión
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # URL para cerrar sesión con redireccionamiento
    path('registro/', RegistroUsuario.as_view(), name='registro'),  # URL para el registro de usuario
]
