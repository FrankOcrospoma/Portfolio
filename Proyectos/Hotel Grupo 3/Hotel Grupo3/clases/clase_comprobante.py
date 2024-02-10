class Comprobante:
    id = 0
    tipo_comprobante = ""
    numero_comprobante = ""
    fecha_comprobante = ""
    monto_total = 0
    transaccion_id = 0
    persona_id = 0
    midic =dict()

    def __init__(self, p_id, p_tipo_comprobante, p_numero_comprobante, p_fecha_comprobante,p_monto_total,p_transaccion_id,p_persona_id):
        self.id = p_id
        self.tipo_comprobante = p_tipo_comprobante
        self.numero_comprobante = p_numero_comprobante
        self.fecha_comprobante = p_fecha_comprobante
        self.monto_total = p_monto_total
        self.transaccion_id = p_transaccion_id
        self.persona_id = p_persona_id

        self.midic["id"] = p_id
        self.midic["tipo_comprobante"] = p_tipo_comprobante
        self.midic["numero_comprobante"] = p_numero_comprobante
        self.midic["fecha_comprobante"] = p_fecha_comprobante
        self.midic["monto_total"] = p_monto_total
        self.midic["transaccion_id"] = p_transaccion_id
        self.midic["persona_id"] = p_persona_id