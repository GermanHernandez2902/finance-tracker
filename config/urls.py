"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # Panel de administración
    path("admin/", admin.site.urls),

    # Autenticación Django (login, logout, etc.)
    path("accounts/", include("django.contrib.auth.urls")),

    # APIs y vistas backend
    path("api/", include("finance.urls")),

    # React frontend (catch-all)
    # Cualquier ruta que NO sea admin, accounts o api
    # devuelve el index.html de React
    re_path(
        r"^(?!admin|accounts|api).*",
        TemplateView.as_view(template_name="frontend/index.html"),
        name="react-app",
    ),
]
