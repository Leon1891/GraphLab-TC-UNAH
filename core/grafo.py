"""Contrato de datos inicial. El Desarrollador 1 podrá extenderlo manteniendo la API."""

import json

MAX_VERTICES = 100
MAX_ARISTAS = 500


def nuevo_grafo():
    return {"vertices": [], "aristas": []}


def _comprobar_nombre(nombre):
    if not isinstance(nombre, str):
        raise ValueError("El nombre del vértice debe ser texto.")
    nombre = nombre.strip()
    if not nombre or len(nombre) > 24:
        raise ValueError("El nombre debe contener entre 1 y 24 caracteres.")
    return nombre


def agregar_vertice(grafo, nombre):
    nombre = _comprobar_nombre(nombre)
    if nombre in grafo["vertices"]:
        raise ValueError(f"El vértice '{nombre}' ya existe.")
    if len(grafo["vertices"]) >= MAX_VERTICES:
        raise ValueError("Se alcanzó el límite de vértices para esta versión.")
    grafo["vertices"].append(nombre)


def agregar_arista(grafo, origen, destino):
    origen, destino = _comprobar_nombre(origen), _comprobar_nombre(destino)
    if origen not in grafo["vertices"] or destino not in grafo["vertices"]:
        raise ValueError("Ambos vértices deben existir.")
    if origen == destino:
        raise ValueError("Esta versión no permite lazos.")
    arista = [origen, destino]
    if arista in grafo["aristas"]:
        raise ValueError("Esta arista dirigida ya existe.")
    if len(grafo["aristas"]) >= MAX_ARISTAS:
        raise ValueError("Se alcanzó el límite de aristas.")
    grafo["aristas"].append(arista)


def eliminar_vertice(grafo, nombre):
    if nombre not in grafo["vertices"]:
        raise ValueError("El vértice no existe.")
    grafo["vertices"].remove(nombre)
    grafo["aristas"] = [e for e in grafo["aristas"] if nombre not in e]


def eliminar_arista(grafo, origen, destino):
    arista = [origen, destino]
    if arista not in grafo["aristas"]:
        raise ValueError("La arista no existe.")
    grafo["aristas"].remove(arista)


def grafo_ejemplo():
    grafo = nuevo_grafo()
    for vertice in ("A", "B", "C", "D", "E"):
        agregar_vertice(grafo, vertice)
    for origen, destino in (("A", "B"), ("A", "D"), ("B", "C"), ("C", "E"), ("D", "E")):
        agregar_arista(grafo, origen, destino)
    return grafo


def exportar_json(grafo):
    return json.dumps({"version": 1, **grafo}, indent=2, ensure_ascii=False)


def importar_json(contenido):
    try:
        datos = json.loads(contenido)
    except (json.JSONDecodeError, TypeError) as exc:
        raise ValueError("No se pudo leer el JSON.") from exc
    if not isinstance(datos, dict) or not isinstance(datos.get("vertices"), list) or not isinstance(datos.get("aristas"), list):
        raise ValueError("El archivo debe contener 'vertices' y 'aristas' como listas.")
    if datos.get("version", 1) != 1:
        raise ValueError("Versión de archivo no compatible.")
    grafo = nuevo_grafo()
    for vertice in datos["vertices"]:
        agregar_vertice(grafo, vertice)
    for arista in datos["aristas"]:
        if not isinstance(arista, list) or len(arista) != 2:
            raise ValueError("Cada arista debe tener la forma [origen, destino].")
        agregar_arista(grafo, arista[0], arista[1])
    return grafo
