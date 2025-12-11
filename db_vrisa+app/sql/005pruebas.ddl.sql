-- Datos de prueba para demostrar sistema multi-institucional
-- ============================================================
-- INSTITUCIÓN 1: Universidad del Valle
-- ============================================================
INSERT INTO usuario (nombre, correo, contrasena, estado)
VALUES (
        'Admin Univalle',
        'admin@univalle.edu',
        'univalle123',
        'activo'
    );
INSERT INTO institucion (nombre, direccion, logo, e_validacion, estado)
VALUES (
        'Universidad del Valle',
        'Calle 13 # 100-00, Cali',
        '',
        'aceptado',
        'activo'
    );
INSERT INTO usuario_institucion (id_i, id_u, rol, e_validacion)
VALUES (1, 1, 'admin', 'aceptado');
-- ============================================================
-- INSTITUCIÓN 2: Alcaldía de Cali
-- ============================================================
INSERT INTO usuario (nombre, correo, contrasena, estado)
VALUES (
        'Admin Alcaldia',
        'admin@cali.gov.co',
        'cali123',
        'activo'
    );
INSERT INTO institucion (nombre, direccion, logo, e_validacion, estado)
VALUES (
        'Alcaldía de Cali',
        'Calle 12 # 1-30, Cali',
        '',
        'aceptado',
        'activo'
    );
INSERT INTO usuario_institucion (id_i, id_u, rol, e_validacion)
VALUES (2, 2, 'admin', 'aceptado');
-- ============================================================
-- ESTACIONES - Universidad del Valle (Institución 1)
-- ============================================================
INSERT INTO estacion (
        nombre,
        ubicacion,
        latitud,
        longitud,
        id_i,
        e_validacion,
        estado
    )
VALUES (
        'Estación Campus Meléndez',
        'Universidad del Valle, Meléndez',
        3.3768,
        -76.5335,
        1,
        'aceptado',
        'activo'
    ),
    (
        'Estación San Fernando',
        'Barrio San Fernando',
        3.3912,
        -76.5347,
        1,
        'en_espera',
        'activo'
    );
-- ============================================================
-- ESTACIONES - Alcaldía de Cali (Institución 2)
-- ============================================================
INSERT INTO estacion (
        nombre,
        ubicacion,
        latitud,
        longitud,
        id_i,
        e_validacion,
        estado
    )
VALUES (
        'Estación Centro',
        'Plaza de Cayzedo',
        3.4372,
        -76.5225,
        2,
        'aceptado',
        'activo'
    ),
    (
        'Estación Norte',
        'Terminal de Autobuses Norte',
        3.4720,
        -76.5304,
        2,
        'en_espera',
        'activo'
    );
-- ============================================================
-- VARIABLES
-- ============================================================
INSERT INTO variable (nombre, tipo_variable, unidad, descripcion)
VALUES (
        'PM2.5',
        'PM2_5',
        'µg/m³',
        'Material particulado fino'
    ),
    (
        'PM10',
        'PM10',
        'µg/m³',
        'Material particulado grueso'
    ),
    (
        'Temperatura',
        'temperatura',
        '°C',
        'Temperatura ambiente'
    );
-- ============================================================
-- SENSORES (para demostración futura)
-- ============================================================
-- Sensor para Estación Campus Meléndez (Univalle)
INSERT INTO sensor (
        id_e,
        nombre,
        modelo,
        api_key,
        estado,
        fecha_alta
    )
VALUES (
        1,
        'Sensor PM Universidad',
        'SDS011',
        'key_univalle_001',
        'activo',
        NOW()
    );
-- Sensor para Estación Centro (Alcaldía)
INSERT INTO sensor (
        id_e,
        nombre,
        modelo,
        api_key,
        estado,
        fecha_alta
    )
VALUES (
        3,
        'Sensor PM Centro',
        'SDS011',
        'key_alcaldia_001',
        'activo',
        NOW()
    );
-- ============================================================
-- MEDICIONES DE EJEMPLO
-- ============================================================
INSERT INTO sensor_variable (id_sen, id_var, tiempo, valor)
VALUES (1, 1, NOW() - INTERVAL '1 hour', 15.5),
    (1, 1, NOW() - INTERVAL '30 minutes', 18.2),
    (1, 1, NOW(), 12.8),
    (2, 1, NOW() - INTERVAL '1 hour', 22.3),
    (2, 1, NOW(), 19.7);