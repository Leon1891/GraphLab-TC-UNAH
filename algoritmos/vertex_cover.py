
from itertools import combinations


MAX_VERTICES_BUSQUEDA = 16


def _obtener_grafo_no_dirigido(grafo):
    """Convierte las aristas dirigidas en aristas no dirigidas únicas."""

    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario.")

    vertices = grafo.get("vertices")
    aristas = grafo.get("aristas")

    if not isinstance(vertices, list) or not isinstance(aristas, list):
        raise ValueError("La estructura del grafo no es válida.")

    if any(not isinstance(v, str) or not v.strip() for v in vertices):
        raise ValueError("Los vértices deben ser nombres válidos.")

    if len(vertices) != len(set(vertices)):
        raise ValueError("No se permiten vértices duplicados.")

    adyacentes = set()

    for arista in aristas:
        if (
            not isinstance(arista, (list, tuple))
            or len(arista) != 2
            or arista[0] not in vertices
            or arista[1] not in vertices
        ):
            raise ValueError("El grafo contiene una arista inválida.")

        a, b = arista
        adyacentes.add(tuple(sorted((a, b))))

    return sorted(vertices), sorted(adyacentes)


def verificar_cobertura(grafo, seleccion, k=None) -> bool:
    """
    Verifica si una selección cubre todas las aristas.

    Si k está definido, la selección no puede superar ese tamaño.
    """

    vertices, aristas = _obtener_grafo_no_dirigido(grafo)

    if not isinstance(seleccion, list):
        raise ValueError("La selección debe ser una lista.")

    if any(v not in vertices for v in seleccion):
        raise ValueError("La selección contiene vértices inexistentes.")

    if len(seleccion) != len(set(seleccion)):
        return False

    if k is not None:
        if not isinstance(k, int) or isinstance(k, bool) or k < 0:
            raise ValueError("K debe ser un entero no negativo.")

        if len(seleccion) > k:
            return False

    seleccionados = set(seleccion)

    return all(
        a in seleccionados or b in seleccionados
        for a, b in aristas
    )


def resolver_vertex_cover(grafo: dict, k: int) -> dict:
    """
    Busca una cobertura de vértices de tamaño máximo K.

    Utiliza búsqueda exhaustiva para grafos pequeños.
    """

    vertices, aristas = _obtener_grafo_no_dirigido(grafo)

    if not isinstance(k, int) or isinstance(k, bool) or k < 0:
        raise ValueError("K debe ser un entero no negativo.")

    if len(vertices) > MAX_VERTICES_BUSQUEDA:
        raise ValueError(
            f"La búsqueda exacta admite como máximo "
            f"{MAX_VERTICES_BUSQUEDA} vértices."
        )

    limite = min(k, len(vertices))

    # Buscar primero coberturas de menor tamaño
    for cantidad in range(limite + 1):

        for candidatos in combinations(vertices, cantidad):

            seleccion = set(candidatos)

            cubre_todo = all(
                a in seleccion or b in seleccion
                for a, b in aristas
            )

            if cubre_todo:
                return {
                    "existe": True,
                    "cobertura": list(candidatos)
                }

    return {
        "existe": False,
        "cobertura": []
    }
