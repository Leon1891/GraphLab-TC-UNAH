"""Pruebas del contrato básico de edición e importación."""

import pytest

from core.grafo import (
    agregar_arista, agregar_vertice, eliminar_arista, eliminar_vertice,
    exportar_json, grafo_ejemplo, importar_json, nuevo_grafo,
)


def test_grafo_vacio():
    assert nuevo_grafo() == {"vertices": [], "aristas": []}


def test_agregar_vertice():
    g = nuevo_grafo()
    agregar_vertice(g, "A")
    assert g["vertices"] == ["A"]


def test_vertice_repetido():
    g = nuevo_grafo()
    agregar_vertice(g, "A")
    with pytest.raises(ValueError):
        agregar_vertice(g, "A")


def test_nombre_vacio():
    with pytest.raises(ValueError):
        agregar_vertice(nuevo_grafo(), " ")


def test_arista_valida():
    g = nuevo_grafo()
    agregar_vertice(g, "A")
    agregar_vertice(g, "B")
    agregar_arista(g, "A", "B")
    assert g["aristas"] == [["A", "B"]]


def test_arista_sin_vertice():
    with pytest.raises(ValueError):
        agregar_arista(nuevo_grafo(), "A", "B")


def test_arista_repetida():
    g = grafo_ejemplo()
    with pytest.raises(ValueError):
        agregar_arista(g, "A", "B")


def test_arista_en_sentido_contrario_es_distinta():
    g = grafo_ejemplo()
    agregar_arista(g, "B", "A")
    assert ["B", "A"] in g["aristas"]


def test_no_permite_lazos():
    g = grafo_ejemplo()
    with pytest.raises(ValueError):
        agregar_arista(g, "A", "A")


def test_eliminar_vertice_elimina_aristas():
    g = grafo_ejemplo()
    eliminar_vertice(g, "A")
    assert "A" not in g["vertices"]
    assert all("A" not in arista for arista in g["aristas"])


def test_eliminar_arista():
    g = grafo_ejemplo()
    eliminar_arista(g, "A", "B")
    assert ["A", "B"] not in g["aristas"]


def test_exportar_importar():
    g = grafo_ejemplo()
    assert importar_json(exportar_json(g)) == g


def test_rechazar_json_invalido():
    with pytest.raises(ValueError):
        importar_json('{no: válido}')


def test_rechazar_vertices_duplicados_desde_json():
    with pytest.raises(ValueError):
        importar_json('{"vertices": ["A", "A"], "aristas": []}')
