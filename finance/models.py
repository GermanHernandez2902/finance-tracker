# Importa el módulo models de Django. 
# models contiene todas las clases necesarias para definir tablas de base de datos.
# Cada clase que hereda de models.Model = una tabla
# Cada atributo = una columna
from django.db import models
# Importa el modelo User que Django trae por defecto para autenticación.
# Este modelo representa: Usuarios registrados y 
# Tiene campos como: username, email, password, etc.
# Esto permite que cada ingreso, gasto y categoría pertenezca a un usuario concreto, 
# cumpliendo el requisito de: “Acceso seguro y aislamiento de datos por usuario”
from django.contrib.auth.models import User

# Create your models here.
# Modelo que representa las categorías financieras (ej: Comida, Alquiler, Freelance)
class Category(models.Model):

    # Nombre de la categoría
    name = models.CharField(max_length=100)

    # Relación con el usuario: cada categoría pertenece a un usuario
    # Si el usuario se elimina, se eliminan también sus categorías
    # .cascade es como un efecto domino Si se elimina el usuario, elimina automáticamente 
    # todos los registros que dependen de él
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Representación en texto del objeto (usado en el admin y depuración)
    def __str__(self):
        return self.name


# Modelo que representa los ingresos del usuario
class Income(models.Model):

    # Usuario al que pertenece el ingreso
    # Garantiza el aislamiento de datos entre usuarios
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Categoría asociada al ingreso
    # Si la categoría se elimina, el ingreso se mantiene sin categoría
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # Cantidad del ingreso (se usa DecimalField para evitar errores en valores monetarios)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Descripción breve del ingreso
    description = models.CharField(max_length=255)

    # Fecha en la que se registró el ingreso
    date = models.DateField()

    # Representación en texto del ingreso
    def __str__(self):
        return f"{self.amount} - {self.date}"


# Modelo que representa los gastos del usuario
class Expense(models.Model):

    # Usuario al que pertenece el gasto
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Categoría asociada al gasto
    # Permite mantener el gasto aunque la categoría sea eliminada
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    # Cantidad del gasto
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Descripción breve del gasto
    description = models.CharField(max_length=255)

    # Fecha en la que se realizó el gasto
    date = models.DateField()

    # Representación en texto del gasto
    def __str__(self):
        return f"{self.amount} - {self.date}"