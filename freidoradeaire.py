from cocina import Cocina
from eficienciaenergetica import EficienciaEnergetica

class FreidoraDeAire(Cocina, EficienciaEnergetica):
    def __init__(self, marca, potencia, consumo_energia, capacidad, nivel_eficiencia, modo_eco, nivel_calor):
        Cocina.__init__(self, marca, potencia, consumo_energia, capacidad)
        EficienciaEnergetica.__init__(self, nivel_eficiencia, modo_eco)
        self._nivel_calor = nivel_calor

    def ajustar_nivel_calor(self):
        return f"Nivel de calor ajustado a {self._nivel_calor}°C en la freidora de aire {self._marca}."
