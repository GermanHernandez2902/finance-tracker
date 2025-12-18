# Importa JsonResponse para devolver respuestas en formato JSON
# Se utiliza para que el frontend (React) pueda consumir los datos
from django.http import JsonResponse

# Decorador que obliga a que el usuario esté autenticado
# Evita que usuarios no autorizados accedan a la API
from django.contrib.auth.decorators import login_required

# Importa los modelos Expense e Income para obtener datos del usuario
from .models import Expense, Income


# Vista API que devuelve los gastos del usuario autenticado en formato JSON
@login_required
def expenses_api(request):

    # Se filtran los gastos para que solo se obtengan los del usuario actual
    # Esto garantiza que cada usuario vea solo su información
    expenses = Expense.objects.filter(user=request.user).values(
        "id",          # Identificador único del gasto (pk)
        "amount",      # Cantidad del gasto
        "description", # Descripción del gasto
        "date"         # Fecha del gasto
    )

    # Se devuelve la lista de gastos como JSON
    # safe=False permite devolver una lista de objetos
    return JsonResponse(list(expenses), safe=False)


# Vista API que devuelve los ingresos del usuario autenticado en formato JSON
@login_required
def incomes_api(request):

    # Se filtran los ingresos para que solo se obtengan los del usuario actual
    incomes = Income.objects.filter(user=request.user).values(
        "id",          # Identificador único del ingreso
        "amount",      # Cantidad del ingreso
        "description", # Descripción del ingreso
        "date"         # Fecha del ingreso
    )

    # Se devuelve la lista de ingresos como JSON
    return JsonResponse(list(incomes), safe=False)


# Vista API que devuelve información básica del usuario autenticado
@login_required
def current_user(request):

    # request.user representa al usuario autenticado por Django
    # Si esta vista se ejecuta, significa que la sesión es válida
    user = request.user

    # Se devuelven solo los datos necesarios para el frontend
    # React usa esto para mostrar el usuario y confirmar autenticación
    return JsonResponse({
        "username": user.username,
        "authenticated": True
    })
