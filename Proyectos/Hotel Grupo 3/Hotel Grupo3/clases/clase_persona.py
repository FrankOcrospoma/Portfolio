class persona:
    persona_id = 0
    dni=""
    numero_telefono = 0
    nombres = ""
    apellidos = ""
    sexo = ""
    fecha_ingreso=""
    fecha_salida = ""
    midic = dict()

    def __init__(self, p_persona_id, p_dni, p_numero_telefono, p_nombres, p_apellidos, p_sexo, p_fecha_ingreso, p_fecha_salida):
        self.persona_id = p_persona_id
        self.dni = p_dni
        self.numero_telefono = p_numero_telefono
        self.nombres = p_nombres
        self.apellidos = p_apellidos
        self.sexo = p_sexo
        self.fecha_ingreso = p_fecha_ingreso
        self.fecha_salida = p_fecha_salida

        self.midic["persona_id"] = p_persona_id
        self.midic["dni"] = p_dni
        self.midic["numero_telefono"] = p_numero_telefono
        self.midic["nombres"] = p_nombres
        self.midic["apellidos"] = p_apellidos
        self.midic["sexo"] = p_sexo
        self.midic["fecha_ingreso"] = p_fecha_ingreso
        self.midic["fecha_salida"] = p_fecha_salida

