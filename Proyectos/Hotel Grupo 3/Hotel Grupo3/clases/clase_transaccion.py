class Transaccion:
    id = 0
    fecha_registro= ""
    hora_registro= ""
    tipo_transaccion  = ""
    fecha_entrada  = ""
    hora_entrada  = ""
    fecha_salida  = ""
    hora_salida   = ""
    habitacion_id = 0
    persona_id = 0
    midic = dict()

    def __init__(self, p_id, p_fecha_registro, p_hora_registro, p_tipo_transaccion,p_fecha_entrada, p_hora_entrada, p_fecha_salida, p_hora_salida,p_habitacion_id,p_persona_id):
        self.id = p_id
        self.fecha_registro = p_fecha_registro
        self.hora_registro = p_hora_registro
        self.tipo_transaccion = p_tipo_transaccion
        self.fecha_entrada = p_fecha_entrada
        self.hora_entrada= p_hora_entrada
        self.fecha_salida = p_fecha_salida
        self.hora_salida = p_hora_salida
        self.habitacion_id = p_habitacion_id
        self.persona_id = p_persona_id
        self.midic["id"] = p_id
        self.midic["fecha_registro"] = p_fecha_registro
        self.midic["hora_registro"] = p_hora_registro
        self.midic["tipo_transaccion"] = p_tipo_transaccion
        self.midic["fecha_entrada"] = p_fecha_entrada
        self.midic["hora_entrada"] = p_hora_entrada
        self.midic["fecha_salida"] = p_fecha_salida
        self.midic["hora_salida"] = p_hora_salida
        self.midic["habitacion"] = p_habitacion_id
        self.midic["personas"] = p_persona_id


        
