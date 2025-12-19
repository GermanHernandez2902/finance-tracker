# Importamos render para devolver páginas HTML usando templates
# Importamos redirect para redirigir a otras vistas
# Importamos get_object_or_404 para obtener objetos o devolver error 404
from django.shortcuts import render, redirect, get_object_or_404

# Importamos el decorador login_required para proteger vistas privadas
from django.contrib.auth.decorators import login_required

# Importamos el modelo Expense para trabajar con los gastos
from .models import Expense

# Importamos el formulario asociado al modelo Expense
from .forms import ExpenseForm


# Vista principal del proyecto (Landing Page)
def landing(request):
    # Creamos un contexto que enviamos al template
    # request.user será el usuario autenticado o AnonymousUser
    context = {
        "user": request.user
    }

    # Renderizamos el template landing.html
    # Esta vista actúa como punto de entrada al sistema
    return render(request, "landing.html", context)


# Vista que muestra la lista de gastos del usuario autenticado
@login_required
def expense_list(request):
    # Filtramos los gastos para que solo se muestren los del usuario actual
    # Esto garantiza privacidad y aislamiento de datos
    expenses = Expense.objects.filter(user=request.user)

    # Renderizamos la plantilla con la lista de gastos
    return render(request, "finance/expense_list.html", {"expenses": expenses})


# Vista para crear un nuevo gasto
@login_required
def expense_create(request):
    # Verificamos si el formulario fue enviado
    if request.method == "POST":
        # Creamos el formulario con los datos enviados
        form = ExpenseForm(request.POST)

        # Validamos que los datos sean correctos
        if form.is_valid():
            # Creamos el objeto sin guardarlo todavía
            # Esto permite asignar el usuario manualmente
            expense = form.save(commit=False)

            # Asignamos el usuario autenticado al gasto
            expense.user = request.user

            # Guardamos el gasto en la base de datos
            expense.save()

            # Redirigimos a la lista de gastos
            return redirect("expense_list")
    else:
        # Si es una petición GET, mostramos el formulario vacío
        form = ExpenseForm()

    # Renderizamos el formulario de creación de gasto
    return render(request, "finance/expense_form.html", {"form": form})


# Vista para eliminar un gasto existente
@login_required
def expense_delete(request, pk):
    # Obtenemos el gasto por su ID y verificamos que pertenezca al usuario
    # Si no existe o no es del usuario, se devuelve un error 404
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    # Eliminamos el gasto de la base de datos
    expense.delete()

    # Redirigimos nuevamente a la lista de gastos
    return redirect("expense_list")
