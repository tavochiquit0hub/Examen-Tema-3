class EficienciaEnergetica:
    def __init__(self, clase_energetica):
        self._clase_energetica = clase_energetica

    def get_clase_energetica(self):
        return self._clase_energetica

    def set_clase_energetica(self, clase_energetica):
        self._clase_energetica = clase_energetica

    def eficiencia(self):
        return f"Este dispositivo tiene una eficiencia energética de clase {self._clase_energetica}."
