
def dfs(grafo: dict, origen: str, destino: str) -> dict:
    """
    Busca una ruta utilizando Depth-First Search (DFS).
    Utiliza una pila para explorar el grafo.
    """

    # 1. Validar el grafo
    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario.")

    vertices = grafo.get("vertices")
    aristas = grafo.get("aristas")

    if not isinstance(vertices, list) or not isinstance(aristas, list):
        raise ValueError("La estructura del grafo no es válida.")

    if origen not in vertices:
        raise ValueError(f"El vértice de origen '{origen}' no existe.")

    if destino not in vertices:
        raise ValueError(f"El vértice de destino '{destino}' no existe.")

    # 2. Construir lista de adyacencia
    adyacencia = {v: [] for v in vertices}

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

    for vecinos in adyacencia.values():
        vecinos.sort()

    # 3. Inicializar la pila
    pila = [origen]
    descubiertos = {origen}
    padres = {origen: None}

    visitados = []
    pasos = []

    # 4. Explorar el grafo
    while pila:

        actual = pila.pop()
        visitados.append(actual)

        if actual != destino:
            # Se insertan en orden inverso para procesar
            # primero el vecino alfabéticamente menor.
            for vecino in reversed(adyacencia[actual]):

                if vecino not in descubiertos:
                    descubiertos.add(vecino)
                    padres[vecino] = actual
                    pila.append(vecino)

        pasos.append({
            "actual": actual,
            "frontera": list(pila),
            "visitados": list(visitados)
        })

        if actual == destino:
            break

    # 5. Reconstruir la ruta
    alcanzable = destino in padres
    ruta = []

    if alcanzable:
        actual = destino

        while actual is not None:
            ruta.append(actual)
            actual = padres[actual]

        ruta.reverse()

    # 6. Devolver resultado
    return {
        "alcanzable": alcanzable,
        "ruta": ruta,
        "visitados": visitados,
        "pasos": pasos
    }
