# Importa JsonResponse para devolver respuestas en formato JSON
# Permite que React consuma datos desde Django
from django.http import JsonResponse

# Importa los modelos necesarios
# Expense e Income representan gastos e ingresos del usuario
from .models import Expense, Income


# Vista API que devuelve los gastos del usuario autenticado
def expenses_api(request):

    # Si el usuario no está autenticado, devolvemos error 401
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Not authenticated"}, status=401)

    # Filtramos los gastos para obtener solo los del usuario actual
    expenses = Expense.objects.filter(user=request.user).values(
        "id",          # Identificador único del gasto
        "amount",      # Monto del gasto
        "description", # Descripción
        "date"         # Fecha
    )

    # Devolvemos la lista de gastos en formato JSON
    return JsonResponse(list(expenses), safe=False)


# Vista API que devuelve los ingresos del usuario autenticado
def incomes_api(request):

    # Verificamos si existe una sesión válida
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "Not authenticated"}, status=401)

    # Filtramos los ingresos del usuario actual
    incomes = Income.objects.filter(user=request.user).values(
        "id",          # Identificador único del ingreso
        "amount",      # Monto del ingreso
        "description", # Descripción
        "date"         # Fecha
    )

    # Devolvemos la lista de ingresos
    return JsonResponse(list(incomes), safe=False)


# Vista API que devuelve información básica del usuario
# React la usa para saber si hay sesión activa
def current_user(request):

    # Si NO hay usuario autenticado
    if not request.user.is_authenticated:
        return JsonResponse(
            {
                "authenticated": False
            },
            status=401
        )

    # Si hay sesión válida, devolvemos datos mínimos del usuario
    return JsonResponse(
        {
            "authenticated": True,
            "username": request.user.username
        }
    )
