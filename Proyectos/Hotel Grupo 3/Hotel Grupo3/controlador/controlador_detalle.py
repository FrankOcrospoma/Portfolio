from bd import obtener_conexion


def insertar_detalle(servicio_id,comprobante_id, monto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle(servicios_id,comprobante_id, monto) VALUES (%s, %s, %s)",
                       (servicio_id,comprobante_id, monto))
    conexion.commit()
    conexion.close()


def obtener_detalle():
    conexion = obtener_conexion()
    detalle = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT servicios_id,comprobante_id,monto FROM detalle")
        detalle = cursor.fetchall()
    conexion.close()
    return detalle


def eliminar_detalle(servicios_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle WHERE servicios_id = %s", (servicios_id,))
    conexion.commit()
    conexion.close()


def obtener_detalle_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT servicios_id,comprobante_id, monto FROM detalle WHERE servicios_id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_detalle(comprobante_id, monto, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle SET comprobante_id = %s, monto = %s WHERE servicios_id = %s",
                       (comprobante_id, monto, id))
    conexion.commit()
    conexion.close()
