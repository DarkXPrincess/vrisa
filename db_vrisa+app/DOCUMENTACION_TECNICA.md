# Documentacion Tecnica - VRISA

## Arquitectura del Sistema

### Stack Tecnologico

El sistema esta construido con las siguientes tecnologias:

- Framework: Django 5.2.9 (Python 3.14)
- Base de Datos: PostgreSQL 16 con extension PostGIS
- Frontend: HTML5, CSS3, Bootstrap 5, JavaScript vanilla
- Containerizacion: Docker y Docker Compose

---

## Modelo de Datos

### Entidades Principales

#### Usuario
```sql
CREATE TABLE usuario (
    id_u SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(200) NOT NULL,
    estado estado DEFAULT 'activo'
);
```

#### Institucion
```sql
CREATE TABLE institucion (
    id_i SERIAL PRIMARY KEY,
    nombre VARCHAR(150) UNIQUE NOT NULL,
    direccion VARCHAR(200),
    logo VARCHAR(200),
    e_validacion validacion DEFAULT 'en_espera',
    estado estado DEFAULT 'activo'
);
```

#### Estacion
```sql
CREATE TABLE estacion (
    id_e SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(200) NOT NULL,
    latitud NUMERIC(10, 7),
    longitud NUMERIC(10, 7),
    geom GEOGRAPHY(Point, 4326),  -- Este campo se genera automaticamente por el trigger
    id_i INT REFERENCES institucion(id_i),
    e_validacion validacion DEFAULT 'en_espera',
    estado estado DEFAULT 'activo'
);
```

### Relaciones entre Tablas

Las relaciones principales del sistema son:

- usuario_institucion: Relacion muchos a muchos entre Usuario e Institucion, incluye el rol del usuario
- estacion.id_i: Llave foranea hacia Institucion (relacion uno a muchos)
- sensor.id_e: Llave foranea hacia Estacion (relacion uno a muchos)
- sensor_variable: Tabla de mediciones que relaciona Sensor con Variable

---

## Sistema de Autenticacion

### Manejo de Sesiones en Django

El sistema utiliza sesiones de Django para mantener el estado del usuario:

```python
# Cuando el login es exitoso
request.session['usuario_id'] = usuario.id_u
request.session['usuario_nombre'] = usuario.nombre

# Para hacer logout
request.session.flush()
```

### Filtrado por Institucion

Cada API verifica los siguientes pasos:
1. Verificar que el usuario este autenticado (revisando usuario_id en la sesion)
2. Obtener el id_i desde la tabla usuario_institucion
3. Filtrar los resultados usando WHERE id_i = <id_institucion>

Ejemplo de codigo:

```python
# Obtener institucion del usuario
usuario_inst = UsuarioInstitucion.objects.get(
    id_u=usuario_id,
    e_validacion='aceptado'
)
# Filtrar estaciones solo de esa institucion
estaciones = Estacion.objects.filter(id_i=usuario_inst.id_i)
```

---

## APIs REST

### Endpoints de Estaciones

La siguiente tabla muestra todos los endpoints disponibles:

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| POST | `/estaciones/registrar/` | Crear nueva estacion |
| GET | `/api/estaciones/pendientes/` | Listar estaciones pendientes (filtrado) |
| GET | `/api/estaciones/activas/` | Listar estaciones aceptadas (filtrado) |
| GET | `/api/estaciones/<id>/` | Obtener detalle de una estacion |
| POST | `/api/estaciones/aceptar/<id>/` | Aprobar una estacion |
| POST | `/api/estaciones/rechazar/<id>/` | Rechazar una estacion |

### Ejemplo: Aprobar una Estacion

Request:
```http
POST /api/estaciones/aceptar/5/
X-CSRFToken: <token>
```

Response:
```json
{
  "mensaje": "Estación 'Campus Meléndez' aceptada exitosamente",
  "estacion_id": 5
}
```

---

## Frontend

### Formulario de Registro

El formulario de registro de estaciones se ve asi:

```html
<form method="POST" action="{% url 'vrisa:registrar_estacion' %}">
    {% csrf_token %}
    <input name="nombre" required>
    <input name="latitud" type="number" step="0.0000001" required>
    <select name="id_i" required>
        <!-- Las opciones se cargan dinamicamente con JavaScript -->
    </select>
</form>
```

### JavaScript Asincrono

El frontend utiliza fetch para comunicarse con las APIs:

```javascript
// Funcion para cargar estaciones pendientes
async function cargarEstacionesPendientes() {
    const response = await fetch('/api/estaciones/pendientes/');
    const estaciones = await response.json();
    // Aqui se renderiza en el DOM
}

// Funcion para aprobar estacion
async function aceptarEstacion(id) {
    await fetch(`/api/estaciones/aceptar/${id}/`, {
        method: 'POST',
        headers: { 'X-CSRFToken': getCookie('csrftoken') }
    });
    cargarEstacionesPendientes(); // Recargar la lista
}
```

---

## PostGIS: Manejo de Coordenadas

### Trigger Automatico

El sistema tiene un trigger que calcula automaticamente el campo geometrico:

```sql
CREATE OR REPLACE FUNCTION fn_set_estacion_geom()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.latitud IS NOT NULL AND NEW.longitud IS NOT NULL THEN
        NEW.geom := ST_SetSRID(
            ST_MakePoint(NEW.longitud, NEW.latitud), 
            4326
        )::geography;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_estacion_geom
    BEFORE INSERT OR UPDATE ON estacion
    FOR EACH ROW EXECUTE FUNCTION fn_set_estacion_geom();
```

Ventaja: El usuario solo necesita ingresar latitud y longitud, el campo geom se calcula solo.

---

## Flujo de Datos del Sistema

El flujo general funciona de la siguiente manera:

1. Usuario anonimo registra una estacion desde el formulario publico
2. Los datos se envian al backend Django
3. Django hace un INSERT en PostgreSQL
4. El trigger se ejecuta automaticamente
5. Se genera el campo geom a partir de latitud y longitud
6. El administrador institucional hace login
7. El backend filtra las estaciones por id_i
8. PostgreSQL devuelve solo las estaciones de esa institucion
9. El administrador puede aceptar o rechazar
10. Se actualiza el campo e_validacion en la base de datos

---

## Seguridad

### Medidas Implementadas

El sistema tiene las siguientes medidas de seguridad:

- Tokens CSRF en todos los formularios POST
- Validacion de sesion en todas las APIs
- Filtrado por institucion para aislar datos entre organizaciones
- Validaciones HTML5 como min, max y required en los inputs

### Pendiente para Produccion

Las siguientes mejoras de seguridad son necesarias antes de poner el sistema en produccion:

- Implementar hash de contraseñas usando la funcion make_password de Django
- Configurar HTTPS obligatorio en el servidor
- Implementar rate limiting para prevenir ataques de fuerza bruta
- Sanitizacion adicional de inputs para prevenir inyeccion SQL

---

## Configuracion Docker

El archivo docker-compose.yml contiene la siguente configuracion:

```yaml
services:
  db:
    image: postgis/postgis:16-3.5
    environment:
      POSTGRES_DB: db_vrisa
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
    volumes:
      - ./sql:/docker-entrypoint-initdb.d
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5433:5432"
```

Ventaja: Los scripts SQL en la carpeta sql/ se ejecutan automaticamente cuando el contenedor inicia por primera vez.

---

## Testing y Verificacion

### Comandos de Verificacion

Aqui hay algunos comandos utiles para verificar que todo funciona:

```bash
# Ver todas las tablas de la base de datos
docker exec -it postgres_django_ejemplo psql -U admin -d db_vrisa \
  -c "\dt"

# Consultar todas las estaciones
docker exec -it postgres_django_ejemplo psql -U admin -d db_vrisa \
  -c "SELECT id_e, nombre, e_validacion, id_i FROM estacion;"

# Ver usuarios y sus instituciones asignadas
docker exec -it postgres_django_ejemplo psql -U admin -d db_vrisa \
  -c "SELECT u.correo, i.nombre, ui.rol 
      FROM usuario u 
      JOIN usuario_institucion ui ON u.id_u = ui.id_u 
      JOIN institucion i ON ui.id_i = i.id_i;"
```

---

## Modelos Django (ORM)

### Configuracion managed=False

Los modelos tienen una configuracion especial:

```python
class Estacion(models.Model):
    id_e = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.DecimalField(max_digits=10, decimal_places=7)
    # ... otros campos
    
    class Meta:
        managed = False  # Django NO gestiona el esquema
        db_table = 'estacion'
```

Implicacion importante: Cualquier cambio en la estructura de las tablas debe hacerse directamente en los archivos SQL, no mediante migraciones de Django.

---

## Deployment y Produccion

### Recomendaciones para Produccion

Cuando se vaya a poner el sistema en produccion, considerar lo siguiente:

1. Servidor: Usar Gunicorn como servidor WSGI con Nginx como proxy inverso
2. Base de Datos: PostgreSQL en un servidor dedicado o servicio administrado
3. Seguridad:
   - Establecer DEBUG = False en settings.py
   - Configurar ALLOWED_HOSTS correctamente
   - Usar variables de entorno para secretos y credenciales
4. Backup: Configurar pg_dump automatico con cron
5. Logging: Implementar sistema de logs centralizado como Sentry

---

## Convenciones de Codigo

El proyecto sigue estas convenciones:

- Nomenclatura en la base de datos: Snake_case (ejemplo: id_e, e_validacion)
- Nomenclatura en Python: PEP8 (ejemplo: api_estaciones_pendientes)
- URLs: Kebab-case (ejemplo: /api/estaciones/pendientes/)
- Comentarios: En español, ya que el equipo de desarrollo es hispanohablante

---

## Referencias Utiles

Documentacion oficial de las tecnologias utilizadas:

- Django: https://docs.djangoproject.com/
- PostGIS: https://postgis.net/documentation/
- Bootstrap: https://getbootstrap.com/docs/5.0/
