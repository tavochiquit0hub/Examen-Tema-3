from cocina import Cocina

class Microondas(Cocina):
    def __init__(self, marca, tipo_combustible, potencia):
        super().__init__(marca, tipo_combustible)
        self._potencia = potencia

    def get_potencia(self):
        return self._potencia

    def set_potencia(self, potencia):
        self._potencia = potencia

    def calentar(self):
        return f"El microondas calienta los alimentos con una potencia de {self._potencia} watts."
