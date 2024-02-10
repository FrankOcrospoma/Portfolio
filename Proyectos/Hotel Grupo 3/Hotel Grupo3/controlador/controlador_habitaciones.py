from bd import obtener_conexion


def insertar_habitacion(estado, descripcion, categoria_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO habitacion(estado_habitacion, descripcion, categoria_id) VALUES (%s, %s, %s)",
                       (estado, descripcion, categoria_id))
    conexion.commit()
    conexion.close()


def obtener_habitacion():
    conexion = obtener_conexion()
    habitaciones = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT h.id, CASE h.estado_habitacion WHEN 'D' THEN 'Disponible' WHEN 'O' THEN 'Ocupada' WHEN 'M' THEN 'Mantenimiento' ELSE 'Estado desconocido' END, h.descripcion, ch.nombre FROM habitacion AS h INNER JOIN categoria_habitacion AS ch ON ch.id = h.categoria_id")
        habitaciones = cursor.fetchall()
    conexion.close()
    return habitaciones


def eliminar_habitacion(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM habitacion WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_habitacion_por_id(id):
    conexion = obtener_conexion()
    habitacion = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT h.id,  CASE h.estado_habitacion WHEN 'D' THEN 'Disponible' WHEN 'O' THEN 'Ocupada' WHEN 'M' THEN 'Mantenimiento' ELSE 'Estado desconocido' END, h.descripcion, ch.id FROM habitacion AS h INNER JOIN categoria_habitacion AS ch ON ch.id = h.categoria_id WHERE h.id = %s", (id,))
        habitacion = cursor.fetchone()
    conexion.close()
    return habitacion



def actualizar_habitacion(estado, descripcion, categoria_id, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE habitacion SET estado_habitacion = %s, descripcion = %s, categoria_id = %s WHERE id = %s",
                       (estado, descripcion, categoria_id, id))
    conexion.commit()
    conexion.close()
