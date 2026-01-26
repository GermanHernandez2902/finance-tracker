# Importamos path para definir rutas
from django.urls import path

# Importamos SOLO las vistas HTML necesarias
from .views import (
    landing,
    dashboard,
)

# Importamos SOLO las vistas de la API
from .api_views import (
    expenses_api,
    incomes_api,
    current_user,
)

urlpatterns = [
    # Landing pública
    path("", landing, name="landing"),

    # Dashboard React protegido
    path("dashboard/", dashboard, name="dashboard"),

    # API para React
    path("api/expenses/", expenses_api, name="expenses_api"),
    path("api/incomes/", incomes_api, name="incomes_api"),
    path("api/user/", current_user, name="current_user"),
]
