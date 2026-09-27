# BASE DE CONOCIMIENTO
rutas = {
    "Portal Norte": ["Calle 146", "Autonorte"],
    "Calle 146": ["Portal Norte", "Calle 127"],
    "Autonorte": ["Portal Norte", "Calle 100"],
    "Calle 127": ["Calle 146", "Calle 100"],
    "Calle 100": ["Autonorte", "Calle 127", "Heroes"],
    "Heroes": ["Calle 100", "Calle 72"],
    "Calle 72": ["Heroes", "Calle 45"],
    "Calle 45": ["Calle 72", "Av Jimenez"],
    "Av Jimenez": ["Calle 45", "Portal Sur"],
    "Portal Sur": ["Av Jimenez"]
}

# FUNCIÓN PARA BUSCAR UNA RUTA
def buscar_ruta(origen, destino, ruta=None):
    if ruta is None:
        ruta = []

    ruta = ruta + [origen]

    # Si llegamos al destino
    if origen == destino:
        return ruta

    # Revisar las estaciones conectadas
    for estacion in rutas[origen]:
        if estacion not in ruta:
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
print(" SISTEMA INTELIGENTE DE RUTAS ")
print("================================")
print("\nEstaciones disponibles:")
print("- Portal Norte - Calle 146 - Autonorte - Calle 127 - Calle 100 - Heroes - Calle 72 - Calle 45 - Av Jimenez - Portal Sur ")

# --- ARREGLO PARA MAYÚSCULAS/MINÚSCULAS ---
origen_input = input("\nIngrese el origen: ").strip()
destino_input = input("Ingrese el destino: ").strip()

# Diccionario que ignora mayúsculas
mapa = {k.lower(): k for k in rutas}
origen = mapa.get(origen_input.lower())
destino = mapa.get(destino_input.lower())

# Validación
if not origen or not destino:
    print("\nLa estación ingresada no existe.")
else:
    resultado = buscar_ruta(origen, destino)
    if resultado:
        print("\nRuta encontrada:")
        print(" -> ".join(resultado))
    else:
        print("\nNo hay ruta.")