from django.urls import path
from . import views

app_name = "vrisa"

urlpatterns = [
    path("", views.index, name="index"),

    # pantalla admin instituciones
    path("panel/instituciones/", views.admin_instituciones, name="V_admin_inst"),

    # pantalla admin sistema
    path("panel/sistema/", views.admin_sistema, name="V_admin_sist"),

    # POST del formulario de institución
    path("instituciones/registrar/", views.registrar_institucion, name="registrar_institucion"),

    # API para listas con JS
    path("api/instituciones/", views.api_instituciones, name="api_instituciones"),

    # 🔹 LOGIN DE USUARIO (la vista login de views.py)
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout_view"),

    path("tableros/", views.tableros, name="tableros"),
]
