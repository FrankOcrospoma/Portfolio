class Categoria_habitacion:
    id = 0
    nombre = ""
    precio = 0
    midic = dict()

    def __init__(self, p_id, p_nombre, p_precio):
        self.id = p_id
        self.nombre = p_nombre
        self.precio = p_precio
        self.midic["id"] = p_id
        self.midic["nombre"] = p_nombre
        self.midic["precio"] = p_precio