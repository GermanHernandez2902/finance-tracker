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
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-dev-key")


# DEBUG controlado por variable de entorno
DEBUG = os.getenv("DEBUG", "False") == "True"


# Hosts permitidos
ALLOWED_HOSTS = ["*"]


# Aplicaciones instaladas
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # App principal
    "finance",
]


# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise para servir React build
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

        # Aquí Django encontrará el index.html de React
        # React build está en: static/frontend/index.html
        "DIRS": [BASE_DIR / "static" / "frontend"],

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
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
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


# ARCHIVOS ESTÁTICOS (React + Django)

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Aquí están los assets generados por Vite (static/frontend/assets)
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# Clave primaria por defecto
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# SESIONES (mismo dominio → cookies OK)

SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_SAMESITE = "Lax"
SESSION_COOKIE_SECURE = True


# CSRF

CSRF_COOKIE_SAMESITE = "Lax"
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://finance-tracker-jl22.onrender.com",
]


# REDIRECCIONES AUTH

LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"
