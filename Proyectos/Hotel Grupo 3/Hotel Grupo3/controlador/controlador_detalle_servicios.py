from bd import obtener_conexion

def insertar_detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio, transaccion_id, servicio_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio, transaccion_id, servicio_id) VALUES (%s, %s, %s, %s, %s, %s)",
                       (fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio, transaccion_id, servicio_id))
    conexion.commit()
    conexion.close()


def obtener_detalle_servicios():
    conexion = obtener_conexion()
    detalle_servicios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT d.id, d.fecha_solicitud, d.hora_solicitud, d.descripcion_solicitud, d.monto_servicio, t.id, s.descripcion FROM detalle_servicios AS d INNER JOIN servicios AS s ON s.id=d.servicio_id INNER JOIN transaccion AS t on t.id=d.transaccion_id")
        detalle_servicios = cursor.fetchall()
    conexion.close()
    return detalle_servicios

def obtener_detalle_servicios_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT d.id, d.fecha_solicitud, d.hora_solicitud, d.descripcion_solicitud, d.monto_servicio, t.id, s.id FROM detalle_servicios AS d INNER JOIN servicios AS s ON  s.id=d.servicio_id INNER JOIN transaccion AS t on t.id=d.transaccion_id WHERE d.id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def eliminar_detalle_servicios(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_servicios WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def actualizar_detalle_servicios(fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio, transaccion_id,servicio_id, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_servicios SET fecha_solicitud = %s, hora_solicitud = %s, descripcion_solicitud  = %s, monto_servicio = %s, transaccion_id = %s, servicio_id = %s WHERE id = %s",
                       (fecha_solicitud, hora_solicitud, descripcion_solicitud, monto_servicio,transaccion_id, servicio_id, id))
    conexion.commit()
    conexion.close()