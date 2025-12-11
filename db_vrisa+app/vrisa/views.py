from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Institucion, Usuario, Estacion
from django.views.decorators.csrf import csrf_exempt

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


def api_institucion_detalle(request, id):
    try:
        inst = Institucion.objects.get(id_i=id)
    except Institucion.DoesNotExist:
        return JsonResponse({"error": "Institución no encontrada"}, status=404)

    data = {
        "id": inst.id_i,
        "nombre": inst.nombre,
        "direccion": inst.direccion,
        "setcolores": inst.setcolores if hasattr(inst, 'setcolores') else None,
        "logo": inst.logo,
        "estado": inst.estado,
        "validacion": inst.e_validacion,
    }
    return JsonResponse(data)

@csrf_exempt
def api_institucion_aceptar(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        inst = Institucion.objects.get(id_i=id)
    except Institucion.DoesNotExist:
        return JsonResponse({"error": "Institución no encontrada"}, status=404)

    inst.e_validacion = "aceptado"
    inst.estado = "activo"
    inst.save()

    return JsonResponse({"mensaje": f"Incripción de {inst.nombre} aprobada."})

@csrf_exempt
def api_institucion_rechazar(request, inst_id):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        inst = Institucion.objects.get(id_i=inst_id)
    except Institucion.DoesNotExist:
        return JsonResponse({"error": "Institución no encontrada"}, status=404)

    # Solo cambiar estado
    inst.e_validacion = "rechazado"
    inst.save()

    return JsonResponse({"mensaje": f"Rechazo de {inst.nombre} efectuado."})


# ============================================================
# GESTIÓN DE ESTACIONES
# ============================================================

def registrar_estacion(request):
    """
    Vista para registrar una nueva estación de monitoreo.
    
    Flujo:
    1. Recibe datos del formulario (POST)
    2. Crea un objeto Estacion en la base de datos
    3. El trigger SQL automáticamente genera el campo 'geom' desde latitud/longitud
    4. Redirige al index con un mensaje de éxito
    """
    
    # Solo procesar si es una petición POST (envío de formulario)
    if request.method == "POST":
        
        # 1. OBTENER DATOS del formulario
        nombre = request.POST.get("nombre")
        ubicacion = request.POST.get("ubicacion")
        latitud = request.POST.get("latitud")
        longitud = request.POST.get("longitud")
        id_i = request.POST.get("id_i")  # ID de la institución
        
        # 2. VALIDACIÓN BÁSICA - Verificar que los campos requeridos existan
        if not all([nombre, ubicacion, latitud, longitud, id_i]):
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect("vrisa:index")
        
        # 3. CREAR la estación en la base de datos
        try:
            Estacion.objects.create(
                nombre=nombre,
                ubicacion=ubicacion,
                latitud=float(latitud),      # Convertir texto a número decimal
                longitud=float(longitud),    # Convertir texto a número decimal
                id_i=int(id_i),              # Convertir texto a número entero
                cert_mant="",                # Certificados por ahora vacíos (Fase 5)
                cert_cal="",
                e_validacion="en_espera",    # Nueva estación debe ser validada
                estado="activo"
            )
            # El campo 'geom' se genera AUTOMÁTICAMENTE por el trigger SQL
            
            messages.success(request, 
                "Estación registrada exitosamente. En espera de validación.")
            
        except Exception as e:
            # Si algo sale mal (ej: institución no existe), mostrar error
            messages.error(request, f"Error al registrar estación: {str(e)}")
        
        return redirect("vrisa:index")
    
    # Si alguien intenta acceder con GET, redireccionar al index
    return redirect("vrisa:index")


def api_estaciones_pendientes(request):
    """
    API para listar las estaciones PENDIENTES de aprobación
    de la INSTITUCIÓN del usuario logueado.
    
    Solo muestra estaciones donde:
    - e_validacion='en_espera' 
    - id_i = institución del usuario actual
    
    Esto asegura que cada admin institucional solo vea SUS estaciones.
    """
    
    # 1. VERIFICAR que el usuario esté logueado
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return JsonResponse({"error": "No autenticado"}, status=401)
    
    # 2. OBTENER la institución del usuario
    try:
        from .models import UsuarioInstitucion
        usuario_inst = UsuarioInstitucion.objects.get(
            id_u=usuario_id,
            e_validacion='aceptado'  # Solo instituciones aceptadas
        )
        id_institucion = usuario_inst.id_i
    except UsuarioInstitucion.DoesNotExist:
        return JsonResponse({"error": "Usuario no tiene institución asignada"}, status=403)
    
    # 3. CONSULTAR estaciones PENDIENTES de ESA institución
    estaciones = Estacion.objects.filter(
        e_validacion='en_espera',
        id_i=id_institucion  # ← FILTRO CLAVE: solo de esta institución
    ).order_by('-id_e')
    
    # 4. CONVERTIR a lista de diccionarios
    data = []
    for estacion in estaciones:
        data.append({
            "id": estacion.id_e,
            "nombre": estacion.nombre,
            "ubicacion": estacion.ubicacion,
            "latitud": float(estacion.latitud) if estacion.latitud else None,
            "longitud": float(estacion.longitud) if estacion.longitud else None,
            "id_institucion": estacion.id_i,
        })
    
    return JsonResponse(data, safe=False)


def api_estacion_detalle(request, id):
    """
    API para ver los DETALLES COMPLETOS de una estación específica.
    
    El admin institucional hace click en una estación de la lista
    y esta API devuelve toda la información para mostrar en un modal.
    
    Parámetro:
        id: El ID de la estación (viene de la URL)
    """
    
    try:
        # 1. BUSCAR la estación por ID
        # .get() es como SELECT * FROM estacion WHERE id_e = {id}
        estacion = Estacion.objects.get(id_e=id)
        
        # 2. CREAR diccionario con TODOS los datos
        data = {
            "id": estacion.id_e,
            "nombre": estacion.nombre,
            "ubicacion": estacion.ubicacion,
            "latitud": float(estacion.latitud) if estacion.latitud else None,
            "longitud": float(estacion.longitud) if estacion.longitud else None,
            "cert_mant": estacion.cert_mant,
            "cert_cal": estacion.cert_cal,
            "e_validacion": estacion.e_validacion,
            "estado": estacion.estado,
            "id_institucion": estacion.id_i,
        }
        
        return JsonResponse(data)
        
    except Estacion.DoesNotExist:
        # Si no existe la estación, devolver error 404
        return JsonResponse({"error": "Estación no encontrada"}, status=404)


def api_estacion_aceptar(request, id):
    """
    API para APROBAR una estación pendiente.
    
    Cambia e_validacion de 'en_espera' a 'aceptado'
    
    Parámetro:
        id: El ID de la estación a aprobar
    """
    
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
    try:
        # 1. BUSCAR la estación
        estacion = Estacion.objects.get(id_e=id)
        
        # 2. CAMBIAR el estado de validación
        estacion.e_validacion = "aceptado"
        estacion.save()  # Guarda los cambios en la base de datos
        
        # 3. CONFIRMAR al frontend
        return JsonResponse({
            "mensaje": f"Estación '{estacion.nombre}' aceptada exitosamente",
            "estacion_id": estacion.id_e
        })
        
    except Estacion.DoesNotExist:
        return JsonResponse({"error": "Estación no encontrada"}, status=404)


def api_estacion_rechazar(request, id):
    """
    API para RECHAZAR una estación pendiente.
    
    Cambia e_validacion de 'en_espera' a 'rechazado'
    
    Parámetro:
        id: El ID de la estación a rechazar
    """
    
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
    try:
        # 1. BUSCAR la estación
        estacion = Estacion.objects.get(id_e=id)
        
        # 2. CAMBIAR el estado de validación
        estacion.e_validacion = "rechazado"
        estacion.save()
        
        # 3. CONFIRMAR al frontend
        return JsonResponse({
            "mensaje": f"Estación '{estacion.nombre}' rechazada",
            "estacion_id": estacion.id_e
        })
        
    except Estacion.DoesNotExist:
        return JsonResponse({"error": "Estación no encontrada"}, status=404)





def api_estaciones_activas(request):
    """API para listar estaciones ACTIVAS de la institución del usuario"""
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return JsonResponse({"error": "No autenticado"}, status=401)
    
    try:
        from .models import UsuarioInstitucion
        usuario_inst = UsuarioInstitucion.objects.get(id_u=usuario_id, e_validacion='aceptado')
        id_institucion = usuario_inst.id_i
    except UsuarioInstitucion.DoesNotExist:
        return JsonResponse({"error": "Usuario no tiene institución"}, status=403)
    
    estaciones = Estacion.objects.filter(
        e_validacion='aceptado',
        id_i=id_institucion,
        estado='activo'
    ).order_by('-id_e')
    
    data = [{"id": e.id_e, "nombre": e.nombre, "ubicacion": e.ubicacion, 
             "latitud": float(e.latitud) if e.latitud else None,
             "longitud": float(e.longitud) if e.longitud else None} for e in estaciones]
    
    return JsonResponse(data, safe=False)