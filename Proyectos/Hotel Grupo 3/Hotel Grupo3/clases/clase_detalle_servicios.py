class Detalle_S:
    id = 0
    fecha_solicitud = ""
    hora_solicitud = ""
    descripcion_solicitud = ""
    monto_servicio = 0
    transaccion_id =0
    servicio_id = 0
    midic = dict()

    def __init__(self,p_id,p_fecha_solicitud,p_hora_solicitud,p_descripcion_solicitud,p_monto_servicio,p_transaccion_id,p_servicio_id):
        self.id = p_id
        self.fecha_solicitud = p_fecha_solicitud
        self.hora_solicitud  = p_hora_solicitud
        self.descripcion = p_descripcion_solicitud
        self.monto_servicio = p_monto_servicio
        self.midic["id"] = p_id
        self.midic["fecha_solicitud"] = p_fecha_solicitud
        self.midic["hora_solicitud"] = p_hora_solicitud
        self.midic["descripcion_solicitud"] = p_descripcion_solicitud
        self.midic["monto_servicio"] = p_monto_servicio
        self.midic["transaccion_id"] = p_transaccion_id
        self.midic["servicio"] = p_servicio_id