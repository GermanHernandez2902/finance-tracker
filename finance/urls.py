# Importa la función path para definir las rutas URL de la aplicación
from django.urls import path

# Importa las vistas tradicionales (HTML) y las vistas de la API (JSON)
# views → vistas que renderizan templates Django
# api_views → vistas que devuelven datos en formato JSON para React
from . import views, api_views


# Definición de las URLs propias de la aplicación finance
urlpatterns = [

    # Ruta raíz del proyecto
    # http://127.0.0.1:8000/
    # Muestra la landing page con la explicación del proyecto
    path("", views.landing, name="landing"),

    # Rutas de vistas tradicionales (HTML)
    path("expenses/", views.expense_list, name="expense_list"),
    path("expenses/new/", views.expense_create, name="expense_create"),
    path("expenses/delete/<int:pk>/", views.expense_delete, name="expense_delete"),

    # Ruta del dashboard principal
    # Esta vista carga el frontend React
    # Está protegida por autenticación en views.py
    path("dashboard/", views.dashboard, name="dashboard"),

    # Rutas de la API consumidas por React
    path("api/expenses/", api_views.expenses_api, name="expenses_api"),
    path("api/incomes/", api_views.incomes_api, name="incomes_api"),
]
