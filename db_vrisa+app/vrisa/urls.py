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
    # API para detalle de institución

    path("api/instituciones/<int:id>", views.api_institucion_detalle, name="api_inst_detalle"),
    #API para aceptar/rechazar institución

    path("api/instituciones/aceptar/<int:id>", views.api_institucion_aceptar, name="api_inst_aceptar"),
    path("api/instituciones/rechazar/<int:inst_id>", views.api_institucion_rechazar, name="api_institucion_rechazar"),
    
]
