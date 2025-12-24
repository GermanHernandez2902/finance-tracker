"""
Django settings for config project.
"""
# Permite leer variables de entorno
import os

# Permite configurar la base de datos desde DATABASE_URL
import dj_database_url

# Importamos Path para manejar rutas del sistema
from pathlib import Path

# BASE_DIR representa la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Clave secreta de Django
# En producción se sobreescribe desde variables de entorno (Render)
SECRET_KEY = "django-insecure-dev-key"

# Modo desarrollo
# En Render se pondrá DEBUG=False vía variable de entorno
DEBUG = True


# Hosts permitidos
# Para deploy inicial en Render permitimos todos
# Luego se puede restringir al dominio real
ALLOWED_HOSTS = ["*"]


# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Apps del proyecto
    "finance",

    # CORS para conexión con React
    "corsheaders",
]


# Middlewares
MIDDLEWARE = [
    # CORS debe ir arriba
    "corsheaders.middleware.CorsMiddleware",

    # Seguridad
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise para servir archivos estáticos en Render
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# URLs principales
ROOT_URLCONF = "config.urls"


# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        # Django buscará templates dentro de cada app (finance/templates)
        "DIRS": [],

        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = "config.wsgi.application"


# Base de datos
# En producción usa PostgreSQL desde Render
# En local usa SQLite si no hay DATABASE_URL
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}



# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Idioma y zona horaria
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True



# ARCHIVOS ESTÁTICOS


# URL pública de archivos estáticos
STATIC_URL = "/static/"

# Carpeta donde Render recolecta los estáticos
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise optimización
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Clave primaria por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# SESIONES


# Sesiones en base de datos
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = False  # En HTTPS real se puede poner True



# CSRF

CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = False  # Render maneja HTTPS



# CORS PARA REACT

CORS_ALLOW_CREDENTIALS = True

# Durante desarrollo y deploy inicial
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]



# REDIRECCIONES DE AUTH

LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"
