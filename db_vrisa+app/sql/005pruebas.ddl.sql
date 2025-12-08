-- Archivo: datos_prueba_minimos.sql
-- Un solo registro por tabla para pruebas básicas

-- 1. Usuario
INSERT INTO usuario (nombre, correo, contrasena, estado) VALUES
('Usuario Prueba', 'test@vrisa.com', 'test123', 'activo');

-- 2. Institución
INSERT INTO institucion (nombre, direccion, logo, e_validacion, estado) VALUES
('Institución Prueba', 'Cali, Colombia', 'logo_prueba.png', 'aceptado', 'activo');

-- 3. Usuario-Institucion (relaciona usuario 1 con institucion 1)
INSERT INTO usuario_institucion (id_i, id_u, rol, e_validacion) VALUES
(1, 1, 'admin', 'aceptado');

-- 4. Estación
INSERT INTO estacion (nombre, cert_mant, cert_cal, ubicacion, geom, e_validacion, estado) VALUES
('Estación Prueba', 'cert_mant.pdf', 'cert_cal.pdf', 'Ubicación Prueba', 
 ST_SetSRID(ST_MakePoint(-76.5225, 3.4516), 4326)::geography, 'aceptado', 'activo');

-- 5. Variable
INSERT INTO variable (nombre, tipo_variable, unidad, descripcion) VALUES
('PM2.5 Prueba', 'PM2_5', 'µg/m³', 'Material particulado fino');

-- 6. Sensor
INSERT INTO sensor (id_e, nombre, modelo, api_key, estado, fecha_alta) VALUES
(1, 'Sensor Prueba', 'Modelo-Test', 'api_key_test', 'activo', NOW());

-- 7. Sensor-Variable (medición)
INSERT INTO sensor_variable (id_sen, id_var, tiempo, valor) VALUES
(1, 1, NOW(), 15.5);

-- 8. Usuario-Estación (opcional - si necesitas esta relación)
INSERT INTO usuario_estacion (id_u, id_e, rol_estacion, inicio) VALUES
(1, 1, 'responsable_tecnico', NOW());
