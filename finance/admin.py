# Importa el módulo admin de Django, que permite gestionar los datos desde 
# el panel de administración
from django.contrib import admin

# Importa los modelos definidos en models.py de esta aplicación
from .models import Category, Income, Expense

# Register your models here.

# Registra el modelo Category en el panel de administración de Django
# Esto permite crear, editar y eliminar categorías desde la interfaz web de admin
admin.site.register(Category)

# Registra el modelo Income en el panel de administración
# Permite gestionar los ingresos directamente desde el admin
admin.site.register(Income)

# Registra el modelo Expense en el panel de administración
# Permite gestionar los gastos desde el admin
admin.site.register(Expense)



