-- LLENA GEOM AUTOMATICAMENTE
CREATE OR REPLACE FUNCTION fn_set_estacion_geom()
RETURNS TRIGGER AS $$
BEGIN
    -- Validaciones básicas de rango
    IF NEW.latitud IS NOT NULL THEN
        IF NEW.latitud < -90 OR NEW.latitud > 90 THEN
            RAISE EXCEPTION 'Latitud inválida (%). Debe estar entre -90 y 90.', NEW.latitud;
        END IF;
    END IF;

    IF NEW.longitud IS NOT NULL THEN
        IF NEW.longitud < -180 OR NEW.longitud > 180 THEN
            RAISE EXCEPTION 'Longitud inválida (%). Debe estar entre -180 y 180.', NEW.longitud;
        END IF;
    END IF;

    -- Si tenemos latitud y longitud, generamos la geometría
    IF NEW.latitud IS NOT NULL AND NEW.longitud IS NOT NULL THEN
        NEW.geom := ST_SetSRID(
                        ST_MakePoint(NEW.longitud, NEW.latitud),
                        4326
                    )::geography;
    ELSE
        -- Si es INSERT sin coords, dejamos geom en NULL
        IF TG_OP = 'INSERT' THEN
            NEW.geom := NULL;
        ELSE
            -- En UPDATE, si no se envían lat/lon nuevas,
            -- mantenemos el valor anterior de geom
            NEW.geom := OLD.geom;
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

---PARA ESTACION INACTIVA, SE DESACTIVAN LOS SENSORES
CREATE OR REPLACE FUNCTION fn_inactivar_sensores_estacion()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.estado = 'inactivo' AND OLD.estado <> 'inactivo' THEN
        UPDATE sensor
        SET estado = 'inactivo'
        WHERE id_e = NEW.id_e;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

--