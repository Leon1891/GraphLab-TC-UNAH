
from collections import deque


def bfs(grafo: dict, origen: str, destino: str) -> dict:
    """
    Busca una ruta entre dos vértices utilizando
    el algoritmo Breadth-First Search (BFS).

    Devuelve:
        alcanzable: indica si existe una ruta.
        ruta: camino encontrado.
        visitados: vértices procesados.
        pasos: estados de la exploración.
    """

    # 1. Validar la estructura del grafo
    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario.")

    if not isinstance(grafo.get("vertices"), list):
        raise ValueError("La lista de vértices no es válida.")

    if not isinstance(grafo.get("aristas"), list):
        raise ValueError("La lista de aristas no es válida.")

    vertices = grafo["vertices"]
    aristas = grafo["aristas"]

    # 2. Validar origen y destino
    if origen not in vertices:
        raise ValueError(f"El vértice de origen '{origen}' no existe.")

    if destino not in vertices:
        raise ValueError(f"El vértice de destino '{destino}' no existe.")

    # 3. Construir la lista de adyacencia
    adyacencia = {vertice: [] for vertice in vertices}

    for arista in aristas:
        if (
            not isinstance(arista, (list, tuple))
            or len(arista) != 2
            or arista[0] not in adyacencia
            or arista[1] not in adyacencia
        ):
            raise ValueError("El grafo contiene una arista inválida.")

        inicio, fin = arista
        adyacencia[inicio].append(fin)

    # Ordenar los vecinos alfabéticamente
    for vecinos in adyacencia.values():
        vecinos.sort()

    # 4. Inicializar estructuras de BFS
    cola = deque([origen])
    descubiertos = {origen}
    padres = {origen: None}

    visitados = []
    pasos = []

    # 5. Explorar el grafo
    while cola:

        actual = cola.popleft()
        visitados.append(actual)

        # Explorar los vecinos si aún no llegamos al destino
        if actual != destino:
            for vecino in adyacencia[actual]:

                if vecino not in descubiertos:
                    descubiertos.add(vecino)
                    padres[vecino] = actual
                    cola.append(vecino)

        # Guardar una fotografía del estado actual
        pasos.append({
            "actual": actual,
            "frontera": list(cola),
            "visitados": list(visitados)
        })

        # Detenerse cuando encontramos el destino
        if actual == destino:
            break

    # 6. Comprobar si existe una ruta
    alcanzable = destino in padres

    ruta = []

    if alcanzable:
        actual = destino

        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]

        ruta.reverse()

    # 7. Devolver el resultado del contrato
    return {
        "alcanzable": alcanzable,
        "ruta": ruta,
        "visitados": visitados,
        "pasos": pasos
    }
