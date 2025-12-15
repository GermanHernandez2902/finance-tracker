# Importa JsonResponse para devolver respuestas en formato JSON
# Se utiliza para que el frontend (React) pueda consumir los datos
from django.http import JsonResponse

# Decorador que obliga a que el usuario esté autenticado
# Evita que usuarios no autorizados accedan a la API
from django.contrib.auth.decorators import login_required

# Importa el modelo Expense para obtener los gastos desde la base de datos
from .models import Expense


# Vista API que devuelve los gastos del usuario autenticado en formato JSON
@login_required
def expenses_api(request):

    # Se filtran los gastos para que solo se obtengan los del usuario actual
    # Esto garantiza el aislamiento de datos entre usuarios
    expenses = Expense.objects.filter(user=request.user).values(
        "id",          # Identificador único del gasto (pk)
        "amount",      # Cantidad del gasto
        "description", # Descripción del gasto
        "date"         # Fecha del gasto
    )

    # Se convierte el QuerySet en una lista y se devuelve como JSON
    # safe=False permite devolver una lista de objetos en lugar de un diccionario
    # Un diccionario tendría más sentido si el endpoint devolviera un único recurso.
    return JsonResponse(list(expenses), safe=False)
