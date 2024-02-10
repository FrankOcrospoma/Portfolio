class Detalle:
    servicio_id= 0
    comprobante_id= 0
    monto = 0
    midic = dict()

    def __init__(self,p_servicio_id, p_comprobante_id, p_monto ):
        self.id = p_servicio_id
        self.comprobante_id = p_comprobante_id
        self.monto = p_monto
        

        self.midic["monto"] = p_monto
        self.midic["comprobante_id"] = p_comprobante_id
        self.midic["servicios_id"] = p_servicio_id
        
