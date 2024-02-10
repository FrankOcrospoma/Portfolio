class Habitacion:
    id = 0
    estado_habitacion = ""
    descripcion = ""
    categoria_id = 0
    midic = dict()

    def __init__(self, p_id, p_estado_habitacion, p_descripcion, p_categoria_id):
        self.id = p_id
        self.estado_habitacion = p_estado_habitacion
        self.descripcion = p_descripcion
        self.categoria_id = p_categoria_id
        self.midic["id"] = p_id
        self.midic["estado_habitacion"] = p_estado_habitacion
        self.midic["descripcion"] = p_descripcion
        self.midic["categoria"] = p_categoria_id

