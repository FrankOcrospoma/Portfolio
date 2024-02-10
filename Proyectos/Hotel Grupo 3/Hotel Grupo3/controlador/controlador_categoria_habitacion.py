from bd import obtener_conexion


def insertar_categoria_habitacion(nombre,  precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO categoria_habitacion(nombre, precio) VALUES (%s, %s)",
                       (nombre, precio))
    conexion.commit()
    conexion.close()


def obtener_categoria_habitacion():
    conexion = obtener_conexion()
    categoria_habitacion = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM categoria_habitacion")
        categoria_habitacion = cursor.fetchall()
    conexion.close()
    return categoria_habitacion


def eliminar_categoria_habitacion(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM categoria_habitacion WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_categoria_habitacion_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, precio FROM categoria_habitacion WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_categoria_habitacion(nombre, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE categoria_habitacion SET nombre = %s, precio = %s WHERE id = %s",
                       (nombre, precio, id))
    conexion.commit()
    conexion.close()
