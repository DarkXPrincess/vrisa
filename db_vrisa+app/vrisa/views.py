from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Institucion
from .models import Usuario

def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        contrasena = request.POST.get("contrasena")

        if not correo or not contrasena:
            messages.error(request, "Debes ingresar correo y contraseña.")
            return redirect("vrisa:index")

        try:
            usuario = Usuario.objects.get(
                correo=correo,
                contrasena=contrasena,
                estado="activo",
            )
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos, o usuario inactivo.")
            return redirect("vrisa:index")

        # guardar datos en la sesión
        request.session["usuario_id"] = usuario.id_u
        request.session["usuario_nombre"] = usuario.nombre

        messages.success(request, f"Bienvenida, {usuario.nombre}")
        # 👇 redirigir AL NOMBRE DE LA RUTA del panel
        return redirect("vrisa:V_admin_sist")

    # si es GET, no mostramos nada especial (el login está en el index)
    return redirect("vrisa:index")

def logout_view(request):
    request.session.flush()
    messages.info(request, "Has cerrado sesión.")
    return redirect("vrisa:index")

def registrar_institucion(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        direccion = request.POST.get("direccion")
        setColores = request.POST.get("set")
        # por ahora ignoramos setcolores y logo; luego vemos dónde guardarlos

        if not nombre or not direccion:
            # podrías mejorar esto con mensajes de error, pero por ahora
            return redirect("vrisa:index")

        # OJO: en el modelo Institucion e_validacion y estado no aceptan NULL
        Institucion.objects.create(
            nombre=nombre,
            direccion=direccion,
           # setColores=setColores,
            logo="",              # de momento vacío
            e_validacion="en_espera",
            estado="activo",
        )
        messages.success(request,"Institución registrada, en espera de validación")
    return redirect("vrisa:index")



def admin_instituciones(request):
    # vista para cargar V_admin_inst.html
    return render(request, "V_admin_inst.html")

def tableros(request):
    
    return render(request,"V_TR.html")



def admin_sistema(request):
    # vista para cargar V_admin_sist.html
    
    return render(request, "V_admin_sist.html")



def api_instituciones(request):
    instituciones = Institucion.objects.all().order_by("nombre")
    data = [
        {"id": inst.id_i, "nombre": inst.nombre}
        for inst in instituciones
    ]
    return JsonResponse(data, safe=False)
