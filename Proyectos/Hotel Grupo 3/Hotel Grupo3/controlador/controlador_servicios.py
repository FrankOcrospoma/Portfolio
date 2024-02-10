from bd import obtener_conexion


def insertar_servicios(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO servicios(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()


def obtener_servicios():
    conexion = obtener_conexion()
    servicios = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, descripcion FROM servicios")
        servicios = cursor.fetchall()
    conexion.close()
    return servicios


def eliminar_servicios(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM servicios WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_servicios_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, descripcion FROM servicios WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_servicios(descripcion, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE servicios SET descripcion = %s WHERE id = %s",
                       (descripcion, id))
    conexion.commit()
    conexion.close()
