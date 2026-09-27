from collections import deque

red_transporte = {
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

def buscar_ruta(origen, destino):
    cola = deque([(origen, [origen])])
    visitados = set()

    while cola:
        estacion_actual, ruta = cola.popleft()

        if estacion_actual == destino:
            return ruta

        if estacion_actual not in visitados:
            visitados.add(estacion_actual)

            for vecino in red_transporteif vecino not in visitados:
                    cola.append((vecino, ruta + [vecino]))

    return None


print("=== SISTEMA INTELIGENTE DE RUTAS ===")

origen = input("Ingrese estación de origen: ")
destino = input("Ingrese estación destino: ")

ruta = buscar_ruta(origen, destino)

if ruta:
    print("\nMejor ruta encontrada:")
    print(" -> ".join(ruta))
else:
    print("No existe una ruta disponible.")
    
