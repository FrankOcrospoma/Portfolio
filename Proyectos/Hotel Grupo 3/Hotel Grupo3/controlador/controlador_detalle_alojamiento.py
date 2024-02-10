from bd import obtener_conexion


def insertar_detalle_alojamiento(transaccion_id,persona_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_alojamiento(transaccion_id,persona_id) VALUES (%s, %s)",
                       (transaccion_id,persona_id))
    conexion.commit()
    conexion.close()


def obtener_detalle_alojamiento():
    conexion = obtener_conexion()
    detalle_alojamiento = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, transaccion_id, pe.dni FROM detalle_alojamiento da inner join personas pe on pe.persona_id=da.persona_id")
        detalle_alojamiento = cursor.fetchall()
    conexion.close()
    return detalle_alojamiento


def eliminar_detalle_alojamiento(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_alojamiento WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_detalle_alojamiento_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, transaccion_id, persona_id FROM detalle_alojamiento WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_detalle_alojamiento(transaccion_id, persona_id, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_alojamiento SET transaccion_id = %s,persona_id = %s WHERE id = %s",
                       (transaccion_id, persona_id, id))
    conexion.commit()
    conexion.close()