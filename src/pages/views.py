import os

from django import get_version
from django.conf import settings
from django.shortcuts import render


# --- Clases de ejemplo ---
class Developer:
    """Representa a un desarrollador."""

    def __init__(self, name, role):
        self.name = name
        self.role = role


class Repository:
    """Representa un repositorio de código."""

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner  # Espera un objeto de tipo Developer


def home(request):
    # --- Instanciación de objetos ---
    main_developer = Developer(name="Hector", role="Estudiante de Django")
    project_repo = Repository(
        name="Fundamentos de Linux e Introducción a Django", owner=main_developer
    )

    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version() + "PROBANDO CAMBIOS",
        "python_ver": os.environ["PYTHON_VERSION"] + "MAS CAMBIOS",
        "repository": project_repo,
    }

    return render(request, "pages/home.html", context)
