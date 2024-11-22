from cocina import Cocina
from eficienciaenergetica import EficienciaEnergetica

class GrillElectrico(Cocina, EficienciaEnergetica):
    def __init__(self, marca, tipo_combustible, clase_energetica, tipo_superficie):
        Cocina.__init__(self, marca, tipo_combustible)
        EficienciaEnergetica.__init__(self, clase_energetica)
        self._tipo_superficie = tipo_superficie

    def get_tipo_superficie(self):
        return self._tipo_superficie

    def set_tipo_superficie(self, tipo_superficie):
        self._tipo_superficie = tipo_superficie

    def grillar(self):
        return f"El grill eléctrico con superficie {self._tipo_superficie} está listo para asar alimentos."
