
"""Módulo para comparar los algoritmos BFS y DFS."""

import time

import streamlit as st

from algoritmos.bfs import bfs
from algoritmos.dfs import dfs
from core.grafo import grafo_ejemplo


def _ejecutar_y_medir(algoritmo, grafo, origen, destino):
    """Ejecuta un algoritmo y mide su tiempo de ejecución."""

    inicio = time.perf_counter()
    resultado = algoritmo(grafo, origen, destino)
    tiempo = time.perf_counter() - inicio

    return resultado, tiempo


def _mostrar_resultado(nombre, resultado, tiempo):
    """Muestra los resultados de un algoritmo."""

    st.subheader(nombre)

    alcanzable = resultado["alcanzable"]
    st.metric(
        "Estado",
        "Alcanzable" if alcanzable else "No alcanzable"
    )

    ruta = resultado["ruta"]
    if ruta:
        st.write("**Ruta encontrada:**", " → ".join(ruta))
    else:
        st.write("**Ruta encontrada:** No existe una ruta.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Vértices visitados", len(resultado["visitados"]))

    with col2:
        st.metric("Pasos registrados", len(resultado["pasos"]))

    with col3:
        st.metric("Tiempo de ejecución", f"{tiempo:.8f} s")

    with st.expander("Ver recorrido completo"):
        st.write("**Orden de visita:**")
        st.write(" → ".join(resultado["visitados"]))

        st.write("**Detalle de los pasos:**")
        st.json(resultado["pasos"])


def mostrar_comparacion():
    """Interfaz de comparación entre BFS y DFS."""

    st.title("Comparación de algoritmos")
    st.caption(
        "Analiza cómo BFS y DFS recorren un mismo grafo "
        "para determinar si existe una ruta."
    )

    # Inicializar el grafo si todavía no existe.
    if "grafo" not in st.session_state:
        st.session_state.grafo = grafo_ejemplo()

    grafo = st.session_state.grafo
    vertices = grafo.get("vertices", [])
    aristas = grafo.get("aristas", [])

    if not vertices:
        st.warning(
            "No hay vértices disponibles. Primero crea un grafo "
            "desde el Editor de grafos."
        )
        return

    st.subheader("Grafo de análisis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Cantidad de vértices", len(vertices))

    with col2:
        st.metric("Cantidad de aristas", len(aristas))

    st.divider()

    st.subheader("Seleccionar recorrido")

    col1, col2 = st.columns(2)

    with col1:
        origen = st.selectbox(
            "Vértice de origen",
            vertices,
            key="comparacion_origen"
        )

    with col2:
        destino = st.selectbox(
            "Vértice de destino",
            vertices,
            index=min(1, len(vertices) - 1),
            key="comparacion_destino"
        )

    st.info(
        "Ambos algoritmos se ejecutarán sobre el mismo grafo "
        "y utilizando los mismos vértices de origen y destino."
    )

    if st.button(
        "Comparar BFS y DFS",
        type="primary",
        use_container_width=True
    ):
        resultado_bfs, tiempo_bfs = _ejecutar_y_medir(
            bfs, grafo, origen, destino
        )

        resultado_dfs, tiempo_dfs = _ejecutar_y_medir(
            dfs, grafo, origen, destino
        )

        st.session_state.resultado_comparacion = {
            "bfs": resultado_bfs,
            "dfs": resultado_dfs,
            "tiempo_bfs": tiempo_bfs,
            "tiempo_dfs": tiempo_dfs,
        }

    comparacion = st.session_state.get("resultado_comparacion")

    if comparacion is None:
        st.warning("Selecciona los vértices y ejecuta la comparación.")
        return

    st.divider()
    st.header("Resultados de la comparación")

    col_bfs, col_dfs = st.columns(2)

    with col_bfs:
        _mostrar_resultado(
            "BFS (Breadth-First Search)",
            comparacion["bfs"],
            comparacion["tiempo_bfs"]
        )

    with col_dfs:
        _mostrar_resultado(
            "DFS (Depth-First Search)",
            comparacion["dfs"],
            comparacion["tiempo_dfs"]
        )

    st.divider()
    st.header("Análisis teórico")

    st.write(
        "Aunque BFS y DFS recorren el grafo de maneras diferentes, "
        "ambos tienen la misma complejidad asintótica."
    )

    st.table({
        "Característica": [
            "Estrategia",
            "Estructura auxiliar",
            "Complejidad temporal",
            "Complejidad espacial",
            "¿Garantiza la ruta más corta?"
        ],
        "BFS": [
            "Explora por niveles.",
            "Cola (FIFO).",
            "O(V + E)",
            "O(V)",
            "Sí, en grafos no ponderados."
        ],
        "DFS": [
            "Profundiza antes de retroceder.",
            "Pila o recursión.",
            "O(V + E)",
            "O(V)",
            "No."
        ]
    })

    st.subheader("Interpretación")

    st.markdown("""
    - **BFS:** visita primero los vértices más cercanos al origen.
      Por eso encuentra una ruta con el menor número de aristas
      cuando el grafo no tiene pesos.

    - **DFS:** continúa explorando una rama hasta donde puede y
      después retrocede. Puede encontrar una ruta, pero no garantiza
      que sea la más corta.

    - **Tiempo:** ambos algoritmos tienen complejidad O(V + E),
      donde V representa la cantidad de vértices y E la cantidad
      de aristas.

    - **Espacio:** ambos pueden necesitar O(V) memoria auxiliar
      para almacenar vértices visitados y estructuras de exploración.
    """)

    st.caption(
        "Nota: los tiempos medidos son orientativos. En grafos pequeños "
        "pueden variar por el entorno de ejecución y no representan "
        "por sí solos la eficiencia general de cada algoritmo."
    )
