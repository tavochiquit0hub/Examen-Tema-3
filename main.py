from horno import Horno
from microondas import Microondas
from grillelectrico import GrillElectrico

def main():
    # Creación de instancias
    horno = Horno("LG", "gas", 65)
    microondas = Microondas("Samsung", "eléctrico", 800)
    grill = GrillElectrico("Philips", "eléctrico", "A+", "antiadherente")

    # Descripción general
    print("Electrodomésticos de cocina:")
    print(horno.descripcion())
    print(microondas.descripcion())
    print(grill.descripcion())
    print()

    # Uso de métodos exclusivos
    print(horno.modo_hornear())
    print(microondas.calentar())
    print(grill.grillar())
    print(grill.eficiencia())  # Método de EficienciaEnergetica
    print(grill.tipo_cocina())  # Método heredado de Cocina

    # Uso de getters y setters
    print("\nActualizando algunos atributos con setters...")
    horno.set_capacidad(70)
    microondas.set_potencia(1000)
    grill.set_tipo_superficie("acero inoxidable")

    print(f"Nueva capacidad del horno: {horno.get_capacidad()} litros")
    print(f"Nuevo nivel de potencia del microondas: {microondas.get_potencia()} watts")
    print(f"Nuevo tipo de superficie del grill: {grill.get_tipo_superficie()}")

if __name__ == "__main__":
    main()
