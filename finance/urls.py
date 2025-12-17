# Importa la función path para definir las rutas URL de la aplicación
from django.urls import path

# Importa las vistas tradicionales (HTML) y las vistas de la API (JSON)
# views → vistas que renderizan templates Django
# api_views → vistas que devuelven datos en formato JSON para React
from . import views, api_views


# Definición de las URLs propias de la aplicación finance
urlpatterns = [

    # Ruta que muestra la lista de gastos del usuario autenticado
    # Renderiza una plantilla HTML con los gastos filtrados por usuario
    path("expenses/", views.expense_list, name="expense_list"),

    # Ruta para crear un nuevo gasto
    # Muestra un formulario y procesa el envío de los datos
    path("expenses/new/", views.expense_create, name="expense_create"),

    # Ruta para eliminar un gasto específico
    # <int:pk> representa la clave primaria del gasto a eliminar
    # Se utiliza para identificar de forma única el registro en la base de datos
    path("expenses/delete/<int:pk>/", views.expense_delete, name="expense_delete"),

    # Ruta de la API que devuelve los gastos en formato JSON
    # Esta vista no renderiza HTML
    # Está pensada para ser consumida por el frontend en React
    # Devuelve únicamente los gastos del usuario autenticado
    path("api/expenses/", api_views.expenses_api, name="expenses_api"),
]

