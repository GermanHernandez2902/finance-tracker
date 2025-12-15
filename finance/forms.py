# Importa el módulo de formularios de Django
from django import forms

# Importa el modelo Expense para generar el formulario automáticamente
from .models import Expense


# Formulario basado en el modelo Expense
# Se utiliza para crear y validar gastos de forma sencilla y segura
class ExpenseForm(forms.ModelForm):

    # Configuración del formulario
    class Meta:

        # Modelo al que está asociado el formulario
        model = Expense

        # Campos del modelo que se mostrarán en el formulario
        # El campo 'user' se excluye para asignarlo automáticamente en la vista
        fields = ["category", "amount", "description", "date"]
