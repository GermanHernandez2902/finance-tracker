"""
URL configuration for config project.
"""

# Importa el panel de administración de Django
from django.contrib import admin

# Importa las funciones necesarias para definir rutas y enlazar otras apps
from django.urls import path, include

# Importa la vista API que devuelve el usuario autenticado
# Esta vista será consumida directamente por React
from finance.api_views import current_user


# URLs principales del proyecto
urlpatterns = [

    # Ruta del panel de administración de Django
    path('admin/', admin.site.urls),

    # Rutas de autenticación proporcionadas por Django
    # Incluye login, logout, cambio y reseteo de contraseña
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta global de la API que devuelve el usuario autenticado
    # React la utiliza para saber si hay una sesión activa
    path("api/user/", current_user),

    # Incluye las URLs de la aplicación finance
    # Se cargan en la raíz del proyecto
    path("", include("finance.urls")),
]
