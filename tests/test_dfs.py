
import pytest

from algoritmos.dfs import dfs
from core.grafo import grafo_ejemplo


def test_ruta_directa():
    r = dfs(grafo_ejemplo(), "A", "B")
    assert r["alcanzable"] is True
    assert r["ruta"] == ["A", "B"]


def test_ruta_valida():
    r = dfs(grafo_ejemplo(), "A", "E")
    assert r["alcanzable"] is True
    assert r["ruta"][0] == "A"
    assert r["ruta"][-1] == "E"


def test_origen_igual_destino():
    r = dfs(grafo_ejemplo(), "A", "A")
    assert r["ruta"] == ["A"]


def test_destino_inalcanzable():
    g = {
        "vertices": ["A", "B", "C"],
        "aristas": [["A", "B"]]
    }
    r = dfs(g, "A", "C")
    assert r["alcanzable"] is False
    assert r["ruta"] == []


def test_grafo_con_ciclo():
    g = {
        "vertices": ["A", "B", "C"],
        "aristas": [
            ["A", "B"],
            ["B", "C"],
            ["C", "A"]
        ]
    }
    r = dfs(g, "A", "C")
    assert r["alcanzable"] is True
    assert len(r["visitados"]) == len(set(r["visitados"]))


def test_origen_inexistente():
    with pytest.raises(ValueError):
        dfs(grafo_ejemplo(), "X", "A")


def test_destino_inexistente():
    with pytest.raises(ValueError):
        dfs(grafo_ejemplo(), "A", "X")


def test_orden_alfabetico():
    g = {
        "vertices": ["A", "C", "B"],
        "aristas": [["A", "C"], ["A", "B"]]
    }
    r = dfs(g, "A", "B")
    assert r["visitados"][:2] == ["A", "B"]


def test_campos_del_contrato():
    r = dfs(grafo_ejemplo(), "A", "E")
    assert set(r) == {
        "alcanzable", "ruta", "visitados", "pasos"
    }


def test_no_modifica_grafo():
    g = grafo_ejemplo()
    copia = {
        "vertices": g["vertices"].copy(),
        "aristas": [e.copy() for e in g["aristas"]]
    }
    dfs(g, "A", "E")
    assert g == copia
