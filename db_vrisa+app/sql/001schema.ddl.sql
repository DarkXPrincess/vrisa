
CREATE EXTENSION IF NOT EXISTS postgis;

-- Estado de validación de registros (instituciones, estaciones, etc.)
CREATE TYPE validacion AS ENUM ('aceptado', 'en_espera', 'rechazado');

-- Estado general de entidades
CREATE TYPE estado AS ENUM ('activo', 'inactivo');

-- Tipos de variables medidas
CREATE TYPE tipo_variable AS ENUM (
    'PM2_5',
    'PM10',
    'SO2',
    'NO2',
    'O3',
    'CO',
    'temperatura',
    'humedad',
    'velocidad_del_viento'
);

-- Roles de usuario dentro de una institución
CREATE TYPE rol_institucion AS ENUM ('admin', 'operador', 'consulta');

-- Roles de usuario dentro de una estación
CREATE TYPE rol_estacion AS ENUM ('responsable_tecnico', 'operador', 'consulta');

--TABLAS
CREATE TABLE usuario (
    id_u         SERIAL PRIMARY KEY,
    nombre       VARCHAR(100) NOT NULL,
    correo       VARCHAR(120) NOT NULL,
    contrasena   VARCHAR(120) NOT NULL,
    estado       estado NOT NULL DEFAULT 'activo',
    fecha_reg    TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT uq_usuario_correo UNIQUE (correo)
);


CREATE TABLE institucion (
    id_i            SERIAL PRIMARY KEY,
    nombre          VARCHAR(150) NOT NULL,
    direccion       VARCHAR(200) NOT NULL,
    logo            VARCHAR(255),                -- ruta o URL del logo
    --setColores      VARCHAR(200),
    e_validacion    validacion NOT NULL DEFAULT 'en_espera',  -- validación por parte del admin del sistema
    estado          estado NOT NULL DEFAULT 'activo',

    CONSTRAINT uq_institucion_nombre UNIQUE (nombre)
);


CREATE TABLE usuario_institucion (
    id_i           INT NOT NULL,
    id_u           INT NOT NULL,
    rol            rol_institucion NOT NULL,
    e_validacion   validacion NOT NULL DEFAULT 'en_espera',
    fecha_asignado TIMESTAMP NOT NULL DEFAULT NOW(),

    PRIMARY KEY (id_i, id_u),

    CONSTRAINT fk_ui_institucion
        FOREIGN KEY (id_i) REFERENCES institucion (id_i),
    CONSTRAINT fk_ui_usuario
        FOREIGN KEY (id_u) REFERENCES usuario (id_u)
);


CREATE TABLE estacion (
    id_e        SERIAL PRIMARY KEY,                     
    nombre      VARCHAR(100) NOT NULL,
    cert_mant   VARCHAR(200),                       
    cert_cal    VARCHAR(200),                       
    ubicacion   VARCHAR(200) NOT NULL,              
    geom        GEOGRAPHY(Point, 4326),            
    e_validacion validacion NOT NULL DEFAULT 'en_espera',  
    estado      estado NOT NULL DEFAULT 'activo'

);


CREATE TABLE usuario_estacion (
    id_u         INT NOT NULL,
    id_e         INT NOT NULL,
    rol_estacion rol_estacion NOT NULL DEFAULT 'responsable_tecnico',
    inicio       TIMESTAMP NOT NULL DEFAULT NOW(),
    final        TIMESTAMP,              
    PRIMARY KEY (id_u, id_e, inicio),

    CONSTRAINT fk_ue_usuario
        FOREIGN KEY (id_u) REFERENCES usuario (id_u),
    CONSTRAINT fk_ue_estacion
        FOREIGN KEY (id_e) REFERENCES estacion (id_e)
);


CREATE TABLE variable (
    id_var        SERIAL PRIMARY KEY,
    nombre        VARCHAR(100) NOT NULL,           
    tipo_variable tipo_variable NOT NULL,         
    unidad        VARCHAR(20) NOT NULL,            
    descripcion   TEXT
);



CREATE TABLE sensor (
    id_sen      SERIAL PRIMARY KEY,
    id_e        INT NOT NULL,
    nombre      VARCHAR(100) NOT NULL,             
    modelo      VARCHAR(100),                      
    api_key     VARCHAR(64),                      
    estado      estado NOT NULL DEFAULT 'activo',
    fecha_alta  TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_sensor_estacion
        FOREIGN KEY (id_e) REFERENCES estacion (id_e)
);


CREATE TABLE sensor_variable (
    id_sen   INT NOT NULL,
    id_var   INT NOT NULL,
    tiempo   TIMESTAMP NOT NULL,
    valor    NUMERIC(12, 4) NOT NULL,

    PRIMARY KEY (id_sen, id_var, tiempo),

    CONSTRAINT fk_sv_sensor
        FOREIGN KEY (id_sen) REFERENCES sensor (id_sen),
    CONSTRAINT fk_sv_variable
        FOREIGN KEY (id_var) REFERENCES variable (id_var)
);

