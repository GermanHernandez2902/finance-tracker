# Importa la función path para definir rutas URL en Django
from django.urls import path

# Importa las vistas del archivo views.py de esta aplicación
from . import views


# Lista de URLs propias de la aplicación finance
urlpatterns = [

    # URL para mostrar la lista de gastos del usuario
    # Cuando el usuario accede a /expenses/, se ejecuta la vista expense_list
    path("expenses/", views.expense_list, name="expense_list"),

    # URL para crear un nuevo gasto
    # Muestra el formulario y procesa el envío del gasto
    path("expenses/new/", views.expense_create, name="expense_create"),

    # URL para eliminar un gasto concreto
    # <int:pk> recibe el identificador del gasto desde la URL
    # Este valor se pasa a la vista expense_delete
    path("expenses/delete/<int:pk>/", views.expense_delete, name="expense_delete"),
    # URL de la API que devuelve los gastos en formato JSON
    # Esta ruta será consumida por el frontend en React
    path("api/expenses/", views.expenses_api, name="expenses_api"),

]
