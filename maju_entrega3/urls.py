from django.contrib import admin
from django.urls import path, include
from contacto.views import pagina_principal
from django.contrib.auth import views as auth_views
from accounts.views import CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name='pagina_principal'),  # URL raíz redirige a la página principal de contacto
    path('accounts/', include('accounts.urls')),  # Incluye las URLs de la app accounts
    path('contacto/', include('contacto.urls')),  # Incluye las URLs de la app contacto
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # URL para iniciar sesión
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='pagina_principal'), name='logout'),
]

# Agrega esta configuración para manejar archivos media durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)