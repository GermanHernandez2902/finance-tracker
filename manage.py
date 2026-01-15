#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    try:
        from django.core.management import execute_from_command_line
        from django.contrib.auth import get_user_model
        from django.db import OperationalError
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc

    # Ejecutamos comandos normales de Django
    execute_from_command_line(sys.argv)

 
    # CREACIÓN AUTOMÁTICA SUPERUSUARIO
   
    try:
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                print("✔ Superusuario creado automáticamente")

    except OperationalError:
        # La base de datos aún no está lista (primer deploy)
        pass


if __name__ == "__main__":
    main()
