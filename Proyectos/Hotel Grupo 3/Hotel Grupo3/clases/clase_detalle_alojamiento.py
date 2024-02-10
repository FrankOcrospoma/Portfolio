class detalle_alojamiento:
    id=0
    transaccion_id = 0
    persona_id = 0
    midic = dict()

    def __init__(self, p_id, p_transaccion_id, p_persona_id):
        self.id = p_id
        self.transaccion_id = p_transaccion_id
        self.persona_id = p_persona_id
        self.midic["id"] = p_id
        self.midic["transaccion_id"] = p_transaccion_id
        self.midic["persona"] = p_persona_id


