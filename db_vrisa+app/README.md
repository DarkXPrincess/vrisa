# VRISA - Sistema de Vigilancia de Calidad del Aire

Sistema Django para gestion de estaciones de monitoreo ambiental con arquitectura multi-institucional.

## Inicio Rapido

### Requisitos
- Python 3.10 o superior
- Docker y Docker Compose
- PostgreSQL 16 con PostGIS

### Instalacion

```bash
# 1. Clonar repositorio
git clone <repo-url>
cd db_vrisa+app

# 2. Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Iniciar base de datos
docker-compose up -d

# 5. Esperar 10 segundos y ejecutar migraciones
Start-Sleep -Seconds 10  # Windows
sleep 10  # Linux/Mac
python manage.py migrate

# 6. Iniciar servidor
python manage.py runserver
```

Acceder a: `http://127.0.0.1:8000/`

## Usuarios de Prueba

### Universidad del Valle
- Email: admin@univalle.edu
- Password: univalle123

### Alcaldia de Cali
- Email: admin@cali.gov.co
- Password: cali123

## Estructura del Proyecto

```
db_vrisa+app/
├── sql/                    # Scripts DDL/DML
│   ├── 001schema.ddl.sql  # Definicion de tablas
│   ├── 002function.sql    # Funciones PostgreSQL
│   ├── 003trigger.sql     # Triggers
│   └── 005pruebas.ddl.sql # Datos de prueba
├── vrisa/                 # App Django principal
│   ├── models.py         # Modelos ORM
│   ├── views.py          # Logica de negocio
│   ├── urls.py           # Rutas
│   └── templates/        # HTML
├── docker-compose.yml     # Configuracion PostgreSQL
└── requirements.txt       # Dependencias Python
```

## Funcionalidades Principales

Las funcionalidades que tiene el sistema son las siguientes:

- Registro publico de estaciones
- Gestion multi-institucional donde cada administrador ve solo sus estaciones
- Aprobacion y rechazo de estaciones pendientes
- Almacenamiento de coordenadas geograficas usando PostGIS
- APIs REST para integracion con el frontend

## Comandos Utiles

```bash
# Reiniciar base de datos (esto borra todo)
docker-compose down -v
docker-compose up -d

# Crear superusuario Django
python manage.py createsuperuser

# Ver logs de PostgreSQL
docker logs postgres_django_ejemplo

# Acceder a PostgreSQL directamente
docker exec -it postgres_django_ejemplo psql -U admin -d db_vrisa
```

## Flujo de Trabajo

El flujo basico del sistema funciona de la siguiente manera:

1. Un usuario anonimo registra una estacion y esta queda en estado "en_espera"
2. El administrador institucional recibe la solicitud
3. El administrador revisa los detalles y puede aceptar o rechazar la estacion
4. Si la estacion es aceptada, cambia a estado "aceptado" y puede comenzar a enviar medicones
5. Las estaciones rechazadas quedan marcadas como "rechazado" en el sistema

## Tecnologias Utilizadas

- Backend: Django 5.2 con Python 3.14
- Base de Datos: PostgreSQL 16 con extension PostGIS
- Frontend: Bootstrap 5 y JavaScript vanilla
- Containerizacion: Docker

## Notas Importantes

Algunas cosas que debes tener en cuenta:

- Las contraseñas estan guardadas en texto plano (esto es solo para desarrollo, no usar en produccion)
- Los modelos Django tienen la opcion managed=False, lo que significa que el esquema se gestiona directamente con SQL
- Existe un trigger llamado fn_set_estacion_geom que calcula automaticamente las coordenadas geograficas cuando se inserta una estacion

## Troubleshooting

**Error: "No module named django"**
Solucion: Asegurate de activar el entorno virtual con .\venv\Scripts\activate

**Error: "Connection refused" al conectar a PostgreSQL**
Solucion: Verifica que Docker este corriendo con el comando docker ps

**Error: CSRF token missing**
Solucion: Intenta hacer un hard refresh en el navegador presionando Ctrl + Shift + R

## Mas Informacion

Para mas detalles sobre la arquitectura y funcionamiento interno del sistema, consulta el archivo DOCUMENTACION_TECNICA.md que esta en la raiz del proyecto.
