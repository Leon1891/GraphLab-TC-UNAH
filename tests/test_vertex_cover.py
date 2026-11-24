
import pytest

from algoritmos.vertex_cover import (
    resolver_vertex_cover,
    verificar_cobertura
)


def triangulo():
    return {
        "vertices": ["A", "B", "C"],
        "aristas": [
            ["A", "B"],
            ["A", "C"],
            ["B", "C"]
        ]
    }


def test_cobertura_valida():
    assert verificar_cobertura(triangulo(), ["A", "B"])


def test_cobertura_invalida():
    assert not verificar_cobertura(triangulo(), ["A"])


def test_resolver_cobertura_existente():
    r = resolver_vertex_cover(triangulo(), 2)
    assert r["existe"] is True
    assert len(r["cobertura"]) <= 2
    assert verificar_cobertura(triangulo(), r["cobertura"])


def test_no_existe_cobertura():
    r = resolver_vertex_cover(triangulo(), 1)
    assert r["existe"] is False
    assert r["cobertura"] == []


def test_grafo_sin_aristas():
    g = {"vertices": ["A", "B"], "aristas": []}
    r = resolver_vertex_cover(g, 0)
    assert r == {"existe": True, "cobertura": []}


def test_ignorar_direccion():
    g = {
        "vertices": ["A", "B"],
        "aristas": [["A", "B"], ["B", "A"]]
    }
    r = resolver_vertex_cover(g, 1)
    assert r["existe"] is True
    assert len(r["cobertura"]) == 1


def test_ignorar_aristas_duplicadas():
    g = {
        "vertices": ["A", "B"],
        "aristas": [["A", "B"], ["A", "B"]]
    }
    r = resolver_vertex_cover(g, 1)
    assert r["existe"] is True


def test_seleccion_con_vertices_repetidos():
    assert not verificar_cobertura(
        triangulo(), ["A", "A"]
    )


def test_seleccion_supera_k():
    assert not verificar_cobertura(
        triangulo(), ["A", "B"], 1
    )


def test_k_cero():
    assert not resolver_vertex_cover(triangulo(), 0)["existe"]


def test_k_negativo():
    with pytest.raises(ValueError):
        resolver_vertex_cover(triangulo(), -1)


def test_k_no_entero():
    with pytest.raises(ValueError):
        resolver_vertex_cover(triangulo(), 1.5)


def test_seleccion_con_vertice_inexistente():
    with pytest.raises(ValueError):
        verificar_cobertura(triangulo(), ["X"])


def test_limite_de_16_vertices():
    g = {
        "vertices": [f"V{i}" for i in range(17)],
        "aristas": []
    }

    with pytest.raises(ValueError):
        resolver_vertex_cover(g, 2)
