# Asignación de responsabilidades

| Desarrollador | Responsabilidad | Directorios |
|---|---|---|
| 1 | Modelo formal, BFS, DFS, Vertex Cover, pruebas y demostraciones | `core/`, `algoritmos/`, `tests/` |
| 2 (interfaz) | Streamlit, editor visual, comparador, métricas, integración y despliegue | `streamlit_app.py`, `interfaz/`, `utilidades/`, `.github/` |

El archivo `core/grafo.py` es un contrato mínimo de integración de la versión 0.1, creado como punto de partida. El Desarrollador 1 puede refactorizarlo siempre que acuerde cambios con el Desarrollador 2. Ambos revisan Pull Requests antes de fusionarlos a `main`.

Los otros dos integrantes colaboran en preparación, revisión y defensa. Todos participan en la defensa oral.
