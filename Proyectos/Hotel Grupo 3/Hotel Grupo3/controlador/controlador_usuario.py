from bd import obtener_conexion

def obtener_usuario():
    conexion = obtener_conexion()
    users = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nomUsuario, contraseña FROM usuario")
        users = cursor.fetchall()
    conexion.close()
    return users