from graphviz import Digraph

# Crear un diagrama de herencia con detalles de atributos y métodos
diagram = Digraph("Estructura de Clases", format="png")
diagram.attr(rankdir="TB")

# Clase base
diagram.node("Electrodomestico",
             "Electrodomestico\n"
             "- marca\n"
             "+ get_marca()\n"
             "+ set_marca()\n"
             "+ descripcion()", shape="box")

# Nivel 2
diagram.node("Cocina",
             "Cocina\n"
             "- tipo_combustible\n"
             "+ get_tipo_combustible()\n"
             "+ set_tipo_combustible()\n"
             "+ tipo_cocina()", shape="box")

# Nivel 3 (Clases hijas de Cocina)
diagram.node("Horno",
             "Horno\n"
             "- capacidad\n"
             "+ get_capacidad()\n"
             "+ set_capacidad()\n"
             "+ modo_hornear()", shape="box")

diagram.node("Microondas",
             "Microondas\n"
             "- potencia\n"
             "+ get_potencia()\n"
             "+ set_potencia()\n"
             "+ calentar()", shape="box")

# Clase con herencia múltiple
diagram.node("GrillElectrico",
             "GrillElectrico\n"
             "- tipo_superficie\n"
             "- clase_energetica\n"
             "+ get_tipo_superficie()\n"
             "+ set_tipo_superficie()\n"
             "+ grillar()\n"
             "+ eficiencia()", shape="box")

# Relación entre las clases
diagram.edge("Electrodomestico", "Cocina")
diagram.edge("Cocina", "Horno")
diagram.edge("Cocina", "Microondas")
diagram.edge("Cocina", "GrillElectrico")
diagram.edge("GrillElectrico", "Electrodomestico")  # Herencia múltiple

# Renderizar el diagrama
output_path = "/mnt/data/Estructura_Clases_Electrodomesticos"
diagram.render(output_path, view=False)
var = output_path + ".png"
