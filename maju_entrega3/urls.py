
# maju_entrega3/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),  # Ruta para manejar la raíz de la aplicación
]
