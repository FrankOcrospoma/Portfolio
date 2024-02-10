from bd import obtener_conexion


def insertar_transaccion(fecha_registro, hora_registro, tipo_transaccion, fecha_entrada,hora_entrada,fecha_salida,hora_salida,habitacion_id,persona_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO transaccion(fecha_registro, hora_registro, tipo_transaccion, fecha_entrada,hora_entrada,fecha_salida,hora_salida,habitacion_id,persona_id) VALUES (%s, %s, %s, %s, %s,%s, %s,%s, %s)",
                       (fecha_registro, hora_registro, tipo_transaccion, fecha_entrada, hora_entrada,fecha_salida,hora_salida,habitacion_id,persona_id))
    conexion.commit()
    conexion.close()


def obtener_transaccion():
    conexion = obtener_conexion()
    transaccion = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT t.id, t.fecha_registro, t.hora_registro,CASE t.tipo_transaccion WHEN 'E' THEN 'Efectivo' WHEN 'T' THEN 'Tarjeta' WHEN 'Y' THEN 'Yape' ELSE 'Estado desconocido' END AS tipo_transaccion, t.fecha_entrada, t.hora_entrada, t.fecha_salida, t.hora_salida, ha.id, ch.dni FROM transaccion AS t INNER JOIN personas AS ch ON ch.persona_id = t.persona_id INNER JOIN habitacion AS ha ON ha.id = t.habitacion_id")
        transaccion = cursor.fetchall()
    conexion.close()
    return transaccion


def eliminar_transaccion(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM transaccion WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_transaccion_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT t.id,t.fecha_registro,t.hora_registro,CASE t.tipo_transaccion WHEN 'E' THEN 'Efectivo' WHEN 'T' THEN 'Tarjeta' WHEN 'Y' THEN 'Yape' ELSE 'Estado desconocido' END AS tipo_transaccion, t.fecha_entrada, t.hora_entrada, t.fecha_salida, t.hora_salida,ha.id, ch.dni FROM transaccion AS t INNER JOIN personas AS ch ON ch.persona_id = t.persona_id INNER JOIN habitacion AS ha ON ha.id = t.habitacion_id WHERE t.id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def actualizar_transaccion(fecha_registro, hora_registro, tipo_transaccion, fecha_entrada, hora_entrada, fecha_salida, hora_salida, habitacion_id, persona_id, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE transaccion SET fecha_registro = %s, hora_registro = %s, tipo_transaccion = %s, fecha_entrada = %s, hora_entrada = %s, fecha_salida = %s, hora_salida = %s, habitacion_id = %s, persona_id = %s WHERE id = %s",
                       (fecha_registro, hora_registro, tipo_transaccion, fecha_entrada, hora_entrada, fecha_salida, hora_salida, habitacion_id, persona_id, id))
    conexion.commit()
    conexion.close()