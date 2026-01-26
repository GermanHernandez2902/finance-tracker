# Importamos render para devolver páginas HTML usando templates
# Importamos redirect para redirigir a otras vistas
# Importamos get_object_or_404 para obtener objetos de forma segura
from django.shortcuts import render, redirect, get_object_or_404

# Importamos FileResponse para servir archivos estáticos (React build)
from django.http import FileResponse

# Importamos Path para manejar rutas del sistema
from pathlib import Path

# Importamos el decorador login_required para proteger vistas privadas
from django.contrib.auth.decorators import login_required

# Importamos el modelo Expense para trabajar con los gastos
from .models import Expense

# Importamos el formulario asociado al modelo Expense
from .forms import ExpenseForm


# Vista principal del proyecto (Landing Page)
def landing(request):
    # Mostramos siempre la landing
    # El template decide qué botones mostrar según autenticación
    return render(request, "landing.html")


# Vista que muestra la lista de gastos del usuario autenticado
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, "finance/expense_list.html", {"expenses": expenses})


# Vista para crear un nuevo gasto
@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expense_list")
    else:
        form = ExpenseForm()

    return render(request, "finance/expense_form.html", {"form": form})


# Vista para eliminar un gasto existente
@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    return redirect("expense_list")


# Vista que sirve el dashboard en React
@login_required
def dashboard(request):
    """
    Esta vista NO renderiza un template Django.
    Sirve directamente el index.html generado por Vite (React build).
    """

    # Ruta absoluta al index.html del build de React
    react_index_path = (
        Path(__file__).resolve().parent.parent
        / "static"
        / "frontend"
        / "index.html"
    )

    # Devolvemos el archivo HTML como respuesta
    return FileResponse(open(react_index_path, "rb"))
