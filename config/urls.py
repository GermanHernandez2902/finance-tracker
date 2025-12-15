"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa el panel de administración de Django
from django.contrib import admin

# Importa las funciones necesarias para definir rutas y enlazar otras apps
from django.urls import path, include


# URLs principales del proyecto
urlpatterns = [

    # Ruta del panel de administración de Django
    path('admin/', admin.site.urls),

    # Rutas de autenticación proporcionadas por Django
    # Incluye login, logout, cambio y reseteo de contraseña
    path('accounts/', include('django.contrib.auth.urls')),

    # Incluye las URLs de la aplicación finance
    # Se cargan en la raíz del proyecto
    path("", include("finance.urls")),
]

