"""
URL configuration for config project.
"""

# Importa el panel de administración de Django
from django.contrib import admin

# Importa las funciones necesarias para definir rutas y enlazar otras apps
from django.urls import path, include


# URLs principales del proyecto
urlpatterns = [

    # Ruta del panel de administración de Django
    path("admin/", admin.site.urls),

    # Rutas de autenticación proporcionadas por Django
    # Incluye login, logout, cambio y reseteo de contraseña
    path("accounts/", include("django.contrib.auth.urls")),

    # Incluye todas las URLs de la aplicación finance
    # finance controla:
    # - Landing page (/)
    # - Vistas HTML
    # - Endpoints API consumidos por React
    path("", include("finance.urls")),
]
