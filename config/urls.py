"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include

# Importamos la vista landing directamente
from finance.views import landing


urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),

    # Autenticación Django (login, logout, etc.)
    path("accounts/", include("django.contrib.auth.urls")),

    # Landing pública
    path("", landing, name="landing"),

    # Rutas de la app finance (HTML + API)
    path("", include("finance.urls")),
]
