from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from accounts.views import RegistroUsuario  

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/registro/', RegistroUsuario.as_view(), name='registro'),  # Ruta para la vista de registro
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    # Otras URLs específicas de contacto
]


