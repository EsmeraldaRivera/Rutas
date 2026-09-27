# ==========================================
# SISTEMA INTELIGENTE DE RUTAS
# ==========================================

# BASE DE CONOCIMIENTO
rutas = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B", "D", "E"],
    "D": ["C"],
    "E": ["C"]
}

# REGLA PARA BUSCAR UNA RUTA
def buscar_ruta(origen, destino, ruta=[]):

    ruta = ruta + [origen]

    # Si llegamos al destino
    if origen == destino:
        return ruta

    # Revisar las estaciones conectadas
    for estacion in rutasif estacion not in ruta:

            nueva_ruta = buscar_ruta(
                estacion,
                destino,
                ruta
            )

            if nueva_ruta:
                return nueva_ruta

    return None


# PROGRAMA PRINCIPAL

print("================================")
print(" SISTEMA INTELIGENTE DE RUTAS")
print("================================")

print("\nEstaciones disponibles:")
print("A - B - C - D - E")

# INPUT
origen = input("\nIngrese el origen: ").upper()
destino = input("Ingrese el destino: ").upper()

# Validación
if origen not in rutas or destino not in rutas:

    print("\nLa estación ingresada no existe.")

else:

    resultado = buscar_ruta(origen, destino)

    if resultado:

        print("\nRuta encontrada:")
        print(" -> ".join(resultado))

        print(
            "\nNúmero de estaciones:",
            len(resultado)
        )

    else:
        print("\nNo existe una ruta.")
