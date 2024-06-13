# urls.py de la aplicación 'contacto'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('exito/<str:nombre>/<str:email>/<str:telefono>/', views.exito, name='exito'),
]
