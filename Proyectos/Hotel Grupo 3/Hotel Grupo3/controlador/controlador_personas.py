from bd import obtener_conexion


def insertar_persona(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso,fecha_salida):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO personas(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso, fecha_salida) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso,fecha_salida))
    conexion.commit()
    conexion.close()


def obtener_personas():
    conexion = obtener_conexion()
    personas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT persona_id, dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso, fecha_salida FROM personas")
        personas = cursor.fetchall()
    conexion.close()
    return personas


def eliminar_persona(persona_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM personas WHERE persona_id = %s", (persona_id,))
    conexion.commit()
    conexion.close()


def obtener_persona_por_id(persona_id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT persona_id, dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso,fecha_salida FROM personas WHERE persona_id = %s", (persona_id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego


def actualizar_persona(dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso,fecha_salida, persona_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE personas SET dni = %s, numero_telefono = %s, nombres = %s, apellidos = %s, sexo = %s, fecha_ingreso = %s, fecha_salida = %s WHERE persona_id = %s",
                       (dni, numero_telefono, nombres, apellidos, sexo, fecha_ingreso,fecha_salida, persona_id))
    conexion.commit()
    conexion.close()
