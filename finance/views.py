# Funciones auxiliares de Django para renderizar plantillas,
# redirigir usuarios y obtener objetos de forma segura
from django.shortcuts import render, redirect, get_object_or_404

# Decorador que exige que el usuario esté autenticado para acceder a la vista
from django.contrib.auth.decorators import login_required

# Importa el modelo Expense para trabajar con los gastos
from .models import Expense

# Importa el formulario asociado al modelo Expense
from .forms import ExpenseForm

# Create your views here.

# Vista que muestra la lista de gastos del usuario autenticado
@login_required
def expense_list(request):

    # Se filtran los gastos para que solo se muestren los del usuario actual
    # Esto garantiza el aislamiento y la privacidad de los datos
    expenses = Expense.objects.filter(user=request.user)

    # Renderiza la plantilla y envía la lista de gastos al frontend
    return render(request, "finance/expense_list.html", {"expenses": expenses})


# Vista para crear un nuevo gasto
@login_required
def expense_create(request):

    # Si el formulario se envía (POST), se procesan los datos
    if request.method == "POST":

        # Se crea el formulario con los datos enviados por el usuario
        form = ExpenseForm(request.POST)

        # Se valida que los datos del formulario sean correctos
        if form.is_valid():

            # Se crea el objeto sin guardarlo aún en la base de datos
            # Esto permite asignar el usuario manualmente
            expense = form.save(commit=False)

            # Se asigna el usuario autenticado al gasto
            expense.user = request.user

            # Se guarda el gasto definitivamente en la base de datos
            expense.save()

            # Tras crear el gasto, se redirige a la lista de gastos
            return redirect("expense_list")

    else:
        # Si es una petición GET, se muestra el formulario vacío
        form = ExpenseForm()

    # Renderiza el formulario de creación de gasto
    return render(request, "finance/expense_form.html", {"form": form})


# Vista para eliminar un gasto existente
@login_required
def expense_delete(request, pk):

    # Se obtiene el gasto por su ID (pk: primary key) y se comprueba que pertenece al usuario
    # Si no existe o no es del usuario, se devuelve un error 404
    expense = get_object_or_404(Expense, pk=pk, user=request.user)

    # Se elimina el gasto de la base de datos
    expense.delete()

    # Tras la eliminación, se redirige a la lista de gastos
    return redirect("expense_list")



