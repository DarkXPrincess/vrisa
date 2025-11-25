-- Tipos ENUM
CREATE TYPE validacion AS ENUM ('aceptado', 'en_espera', 'rechazado');
CREATE TYPE estado AS ENUM ('activo', 'inactivo');
CREATE TYPE medida AS ENUM ('PM2_5', 'PM10', 'SO2', 'NO2', 'O3', 'CO');
CREATE TYPE tipo_var AS ENUM ('temperatura', 'humedad', 'velocidad_del_viento');

-- ESTACION
CREATE TABLE estacion (
    id_e      SERIAL PRIMARY KEY,
    nombre    VARCHAR(100) NOT NULL,
    cert_mant VARCHAR(200),
    cert_cal  VARCHAR(200),
    ubicacion VARCHAR(100) NOT NULL
);

-- INSTITUCION
CREATE TABLE institucion (
    id_i        SERIAL PRIMARY KEY,
    e_validacion validacion,
    direccion   VARCHAR(100) NOT NULL,
    nombre      VARCHAR(200) NOT NULL,
    logo        VARCHAR(300) NOT NULL
);

-- USUARIO
CREATE TABLE usuario (
    id_u      SERIAL PRIMARY KEY,
    telefono  CHAR(10) NOT NULL,
    correo    VARCHAR(200) NOT NULL,
    nombre    VARCHAR(100) NOT NULL,
    contrasena CHAR(8)      -- mejor sin ñ para no tener que usar comillas
);

-- VARIABLE
CREATE TABLE variable (
    id_var        SERIAL PRIMARY KEY,
    ran_min       INT,
    ran_max       INT,
    descripcion   VARCHAR(300),
    unidad_medida medida,
    tipo_variable tipo_var
);

-- SENSOR
CREATE TABLE sensor (
    id_sen      SERIAL PRIMARY KEY,
    id_e        INT NOT NULL,
    tipo_sensor VARCHAR(100),
    fecha_cal   TIMESTAMP,
    fecha_mant  TIMESTAMP,
    estado      estado,
    CONSTRAINT fk_sensor_estacion
        FOREIGN KEY (id_e) REFERENCES estacion(id_e)
);

-- USUARIO - INSTITUCION (HAS)
CREATE TABLE usuario_institucion (
    id_i        INT NOT NULL,
    id_u        INT NOT NULL,
    rol         VARCHAR(50),
    e_validacion validacion,
    PRIMARY KEY (id_i, id_u),
    CONSTRAINT fk_ui_institucion
        FOREIGN KEY (id_i) REFERENCES institucion(id_i),
    CONSTRAINT fk_ui_usuario
        FOREIGN KEY (id_u) REFERENCES usuario(id_u)
);

-- SENSOR - VARIABLE (MEASURE)
CREATE TABLE sensor_variable (
    id_sen INT NOT NULL,
    id_var INT NOT NULL,
    tiempo TIMESTAMP,
    valor  FLOAT,
    PRIMARY KEY (id_sen, id_var, tiempo),  -- o (id_sen, id_var) como en el diagrama
    CONSTRAINT fk_sv_sensor
        FOREIGN KEY (id_sen) REFERENCES sensor(id_sen),
    CONSTRAINT fk_sv_variable
        FOREIGN KEY (id_var) REFERENCES variable(id_var)
);

-- USUARIO - ESTACION (RESPONSABLE)
CREATE TABLE usuario_estacion (
    id_u         INT NOT NULL,
    id_e         INT NOT NULL,
    rol_estacion VARCHAR(50),
    inicio       TIMESTAMP,
    final        TIMESTAMP,
    PRIMARY KEY (id_u, id_e),
    CONSTRAINT fk_ue_usuario
        FOREIGN KEY (id_u) REFERENCES usuario(id_u),
    CONSTRAINT fk_ue_estacion
        FOREIGN KEY (id_e) REFERENCES estacion(id_e)
);
