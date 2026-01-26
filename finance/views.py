# Importamos FileResponse para servir archivos estáticos
from django.http import FileResponse

# Importamos Path para manejar rutas del sistema
from pathlib import Path

# Importamos redirect
from django.shortcuts import redirect

# Importamos login_required
from django.contrib.auth.decorators import login_required


# Vista raíz del proyecto
def landing(request):
    """
    Sirve directamente el index.html generado por React (Vite build).
    """
    react_index_path = (
        Path(__file__).resolve().parent.parent
        / "static"
        / "frontend"
        / "index.html"
    )

    return FileResponse(open(react_index_path, "rb"))


# Vista del dashboard (React)
@login_required
def dashboard(request):
    """
    Sirve el mismo index.html de React.
    React se encarga del routing interno.
    """
    react_index_path = (
        Path(__file__).resolve().parent.parent
        / "static"
        / "frontend"
        / "index.html"
    )

    return FileResponse(open(react_index_path, "rb"))
