
import pytest

from algoritmos.bfs import bfs
from core.grafo import grafo_ejemplo


def test_ruta_directa():
    resultado = bfs(grafo_ejemplo(), "A", "B")

    assert resultado["alcanzable"] is True
    assert resultado["ruta"] == ["A", "B"]


def test_ruta_minima():
    resultado = bfs(grafo_ejemplo(), "A", "E")

    assert resultado["ruta"] == ["A", "D", "E"]


def test_origen_igual_destino():
    resultado = bfs(grafo_ejemplo(), "A", "A")

    assert resultado["alcanzable"] is True
    assert resultado["ruta"] == ["A"]


def test_destino_inalcanzable():
    grafo = {
        "vertices": ["A", "B", "C"],
        "aristas": [["A", "B"]]
    }

    resultado = bfs(grafo, "A", "C")

    assert resultado["alcanzable"] is False
    assert resultado["ruta"] == []


def test_grafo_con_ciclo():
    grafo = {
        "vertices": ["A", "B", "C"],
        "aristas": [
            ["A", "B"],
            ["B", "C"],
            ["C", "A"]
        ]
    }

    resultado = bfs(grafo, "A", "C")

    assert resultado["ruta"] == ["A", "B", "C"]
    assert len(resultado["visitados"]) == len(set(resultado["visitados"]))


def test_origen_inexistente():
    with pytest.raises(ValueError):
        bfs(grafo_ejemplo(), "X", "A")


def test_destino_inexistente():
    with pytest.raises(ValueError):
        bfs(grafo_ejemplo(), "A", "X")


def test_vecinos_ordenados():
    grafo = {
        "vertices": ["A", "C", "B"],
        "aristas": [["A", "C"], ["A", "B"]]
    }

    resultado = bfs(grafo, "A", "C")

    assert resultado["pasos"][0]["frontera"] == ["B", "C"]


def test_no_modifica_grafo():
    grafo = grafo_ejemplo()
    copia = {
        "vertices": grafo["vertices"].copy(),
        "aristas": [arista.copy() for arista in grafo["aristas"]]
    }

    bfs(grafo, "A", "E")

    assert grafo == copia


def test_campos_del_contrato():
    resultado = bfs(grafo_ejemplo(), "A", "E")

    assert set(resultado.keys()) == {
        "alcanzable", "ruta", "visitados", "pasos"
    }
