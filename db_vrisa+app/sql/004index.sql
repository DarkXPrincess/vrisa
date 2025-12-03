CREATE INDEX idx_estacion_geom ON estacion USING GIST (geom);
CREATE INDEX idx_sv_tiempo ON sensor_variable (tiempo);
CREATE INDEX idx_sv_idvar_tiempo ON sensor_variable (id_var, tiempo);
CREATE INDEX idx_sv_idsen_tiempo ON sensor_variable (id_sen, tiempo);
