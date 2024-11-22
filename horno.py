from cocina import Cocina

class Horno(Cocina):
    def __init__(self, marca, tipo_combustible, capacidad):
        super().__init__(marca, tipo_combustible)
        self._capacidad = capacidad

    def get_capacidad(self):
        return self._capacidad

    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    def modo_hornear(self):
        return f"El horno tiene una capacidad de {self._capacidad} litros y está listo para hornear."
