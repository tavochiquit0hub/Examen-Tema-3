class Electrodomestico:
    def __init__(self, marca):
        self._marca = marca

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def descripcion(self):
        return f"Este es un electrodoméstico de la marca {self._marca}."
