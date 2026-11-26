
from itertools import combinations


MAX_VERTICES_BUSQUEDA = 16


def _obtener_grafo_no_dirigido(grafo):
    """
    Valida el grafo y convierte sus aristas dirigidas
    en aristas no dirigidas únicas.
    """

    if not isinstance(grafo, dict):
        raise ValueError("El grafo debe ser un diccionario.")

    vertices = grafo.get("vertices")
    aristas = grafo.get("aristas")

    if not isinstance(vertices, list) or not isinstance(aristas, list):
        raise ValueError("La estructura del grafo no es válida.")

    # Validar nombres de los vértices
    if any(not isinstance(v, str) or not v.strip() for v in vertices):
        raise ValueError("Los vértices deben ser nombres válidos.")

    # Validar que no existan vértices repetidos
    if len(vertices) != len(set(vertices)):
        raise ValueError("No se permiten vértices duplicados.")

    adyacentes = set()

    # Validar y normalizar las aristas
    for arista in aristas:

        if (
            not isinstance(arista, (list, tuple))
            or len(arista) != 2
            or arista[0] not in vertices
            or arista[1] not in vertices
        ):
            raise ValueError("El grafo contiene una arista inválida.")

        a, b = arista

        # Convertir la arista en no dirigida
        # y eliminar duplicados
        adyacentes.add(tuple(sorted((a, b))))

    return sorted(vertices), sorted(adyacentes)


def verificar_cobertura(grafo, seleccion, k=None) -> bool:
    """
    Verifica si una selección de vértices cubre todas las aristas.

    Una arista está cubierta cuando al menos uno de sus
    extremos pertenece a la selección.

    Si se proporciona k, la selección no puede superar
    esa cantidad de vértices.
    """

    vertices, aristas = _obtener_grafo_no_dirigido(grafo)

    if not isinstance(seleccion, list):
        raise ValueError("La selección debe ser una lista.")

    # Comprobar que los vértices seleccionados existen
    if any(v not in vertices for v in seleccion):
        raise ValueError("La selección contiene vértices inexistentes.")

    # No permitir vértices repetidos
    if len(seleccion) != len(set(seleccion)):
        return False

    # Validar K si fue proporcionado
    if k is not None:

        if not isinstance(k, int) or isinstance(k, bool) or k < 0:
            raise ValueError("K debe ser un entero no negativo.")

        if len(seleccion) > k:
            return False

    seleccionados = set(seleccion)

    # Comprobar que todas las aristas estén cubiertas
    return all(
        a in seleccionados or b in seleccionados
        for a, b in aristas
    )


def resolver_vertex_cover(grafo: dict, k: int) -> dict:
    """
    Busca una cobertura de vértices de tamaño máximo K.

    Utiliza búsqueda exhaustiva mediante combinaciones.

    Busca primero las coberturas más pequeñas para encontrar
    una solución mínima dentro del límite K.

    La búsqueda exacta admite como máximo 16 vértices.
    """

    vertices, aristas = _obtener_grafo_no_dirigido(grafo)

    # Validar K
    if not isinstance(k, int) or isinstance(k, bool) or k < 0:
        raise ValueError("K debe ser un entero no negativo.")

    # Limitar el tamaño del grafo
    if len(vertices) > MAX_VERTICES_BUSQUEDA:
        raise ValueError(
            f"La búsqueda exacta admite como máximo "
            f"{MAX_VERTICES_BUSQUEDA} vértices."
        )

    limite = min(k, len(vertices))

    # Probar coberturas desde tamaño 0 hasta K
    for cantidad in range(limite + 1):

        # Generar todas las combinaciones posibles
        for candidatos in combinations(vertices, cantidad):

            seleccion = set(candidatos)

            # Comprobar si todas las aristas están cubiertas
            cubre_todo = all(
                a in seleccion or b in seleccion
                for a, b in aristas
            )

            if cubre_todo:
                return {
                    "existe": True,
                    "cobertura": list(candidatos)
                }

    # No se encontró ninguna cobertura dentro del límite K
    return {
        "existe": False,
        "cobertura": []
    }
