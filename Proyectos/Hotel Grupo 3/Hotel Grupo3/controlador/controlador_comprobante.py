from bd import obtener_conexion

def insertar_comprobante(tipo_comprobante,numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO comprobante(tipo_comprobante, numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id) VALUES (%s, %s,%s, %s, %s, %s)",
                       (tipo_comprobante,numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id))
    conexion.commit()
    conexion.close()

def obtener_comprobante():#Dar formato a fecha
    conexion = obtener_conexion()
    comprobante = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,  CASE tipo_comprobante WHEN 'B' THEN 'Boleta' WHEN 'F' THEN 'Factura' WHEN 'T' THEN 'Ticket' ELSE 'Estado desconocido' END, numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id FROM comprobante")
        comprobante = cursor.fetchall()
    conexion.close()
    return comprobante

def eliminar_comprobante(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM comprobante WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_comprobante_por_id(id):#Dar formato a fecha
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id,  CASE tipo_comprobante WHEN 'B' THEN 'Boleta' WHEN 'F' THEN 'Factura' WHEN 'T' THEN 'Ticket' ELSE 'Estado desconocido' END, numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id FROM comprobante WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return juego

def actualizar_comprobante(tipo_comprobante,numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE comprobante SET tipo_comprobante = %s, numero_comprobante = %s,fecha_comprobante = %s,monto_total = %s,transaccion_id = %s,persona_id = %s WHERE id = %s",
                       (tipo_comprobante, numero_comprobante,fecha_comprobante,monto_total,transaccion_id,persona_id, id))
    conexion.commit()
    conexion.close()