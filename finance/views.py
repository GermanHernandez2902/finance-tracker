# Importamos render para devolver templates HTML
from django.shortcuts import render, redirect

# Importamos login_required para proteger vistas
from django.contrib.auth.decorators import login_required


# Vista raíz del proyecto
def landing(request):
    """
    Página pública de inicio del proyecto.
    Renderiza el template Django landing.html.
    """
    return render(request, "landing.html")


# Vista del dashboard (protegida)
@login_required
def dashboard(request):
    """
    Punto de entrada al dashboard.
    Por ahora renderiza una vista Django.
    React se integrará después como frontend separado.
    """
    return render(request, "dashboard.html")
