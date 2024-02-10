class Servicios:
    id = 0
    descripcion = ""
    midic = dict()

    def __init__(self, p_id, p_descripcion):
        self.id = p_id
        self.descripcion = p_descripcion
        self.midic["id"] = p_id
        self.midic["descripcion"] = p_descripcion