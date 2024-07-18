from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.user_profile, name='user_profile'),
    # Otras rutas de datos_extra
]
