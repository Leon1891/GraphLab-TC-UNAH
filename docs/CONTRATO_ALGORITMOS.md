# Contrato de integración (Dev. 1 ↔ Dev. 2)

## Representación común
El grafo dirigido es un diccionario sin pesos:

```python
{
    "vertices": ["A", "B", "C"],
    "aristas": [["A", "B"], ["B", "C"]]
}
```

No modificar los datos de entrada dentro de los algoritmos. El editor ya puede exportar/importar JSON con esta forma.

## Funciones que implementará el Desarrollador 1

```python
# algoritmos/bfs.py
bfs(grafo: dict, origen: str, destino: str) -> dict

# algoritmos/dfs.py
dfs(grafo: dict, origen: str, destino: str) -> dict
```

Ambas devolverán:

```python
{
    "alcanzable": True,
    "ruta": ["A", "B", "C"],
    "visitados": ["A", "B", "C"],
    "pasos": [
        {"actual": "A", "frontera": ["B"], "visitados": ["A"]},
        {"actual": "B", "frontera": ["C"], "visitados": ["A", "B"]},
        {"actual": "C", "frontera": [], "visitados": ["A", "B", "C"]}
    ]
}
```

* `ruta=[]` si no hay camino; `ruta=[origen]` cuando origen=destino.
* `visitados` debe contener cada vértice procesado una sola vez.
* `pasos` debe permitir reproducir visualmente la exploración.
* Elegir vecinos por orden alfabético para resultados deterministas.
* Validar que origen y destino existan.

## Problema de decisión

```python
# algoritmos/vertex_cover.py
resolver_vertex_cover(grafo: dict, k: int) -> dict
verificar_cobertura(grafo: dict, seleccion: list[str], k: int | None = None) -> bool
```

La representación de la interfaz es dirigida. Para Vertex Cover se ignorará la orientación y se fusionarán duplicados de aristas. `resolver_vertex_cover` devuelve `{ "existe": bool, "cobertura": list[str] }`, con cobertura vacía si no existe. El máximo inicial de búsqueda exacta es 16 vértices.

## Aceptación
Pruebas de ruta directa, inexistencia, origen=destino, ciclos, BFS mínimo en número de aristas, DFS válida, y coberturas correctas e incorrectas.
