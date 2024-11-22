from electrodomestico import Electrodomestico

class Cocina(Electrodomestico):
    def __init__(self, marca, tipo_combustible):
        super().__init__(marca)
        self._tipo_combustible = tipo_combustible

    def get_tipo_combustible(self):
        return self._tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def tipo_cocina(self):
        return f"Esta cocina funciona con {self._tipo_combustible}."
