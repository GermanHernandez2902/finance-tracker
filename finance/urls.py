# Importamos path para definir rutas
from django.urls import path

# Importamos SOLO las vistas HTML
from .views import (
    landing,
    dashboard,
    expense_list,
    expense_create,
    expense_delete,
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

    # Vistas HTML tradicionales
    path("expenses/", expense_list, name="expense_list"),
    path("expenses/new/", expense_create, name="expense_create"),
    path("expenses/delete/<int:pk>/", expense_delete, name="expense_delete"),

    # API para React
    path("api/expenses/", expenses_api, name="expenses_api"),
    path("api/incomes/", incomes_api, name="incomes_api"),
    path("api/user/", current_user, name="current_user"),
]
