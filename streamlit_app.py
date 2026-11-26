
"""Punto de entrada principal de GraphLab TC."""

import streamlit as st

from interfaz.editor import mostrar_editor
from interfaz.explorador import (
    mostrar_explorador,
    mostrar_vertex_cover,
)
from interfaz.comparacion import mostrar_comparacion


# Configuración general
st.set_page_config(
    page_title="GraphLab TC | UNAH",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Navegación principal
with st.sidebar:
    st.title("🕸️ GraphLab TC")
    st.caption("ISC-312 · Teoría de la Computación | UNAH")

    st.divider()

    pagina = st.radio(
        "Navegación",
        [
            "Editor de grafos",
            "Exploración BFS/DFS",
            "Comparación",
            "Vertex Cover",
            "Acerca del proyecto",
        ],
    )

    st.divider()

    st.caption("Versión 1.0.0 · UNAH")


# Mostrar la sección seleccionada
if pagina == "Editor de grafos":

    mostrar_editor()

elif pagina == "Exploración BFS/DFS":

    mostrar_explorador()

elif pagina == "Comparación":

    mostrar_comparacion()

elif pagina == "Vertex Cover":

    mostrar_vertex_cover()

elif pagina == "Acerca del proyecto":

    st.title("Acerca de GraphLab TC")

    st.markdown("""
    ### Explorador de grafos, alcanzabilidad y problemas de decisión

    **GraphLab TC** es una aplicación educativa desarrollada
    para la asignatura Teoría de la Computación de la
    Universidad Nacional Autónoma de Honduras (UNAH).

    Permite construir y visualizar grafos dirigidos,
    explorar problemas de alcanzabilidad y estudiar
    problemas de decisión mediante algoritmos.

    ### Módulos principales

    - **Editor de grafos:** creación, modificación,
      importación y exportación de grafos.
    - **Exploración BFS/DFS:** búsqueda de rutas y
      análisis de alcanzabilidad.
    - **Comparación:** análisis de los recorridos,
      tiempos de ejecución y complejidad.
    - **Vertex Cover:** resolución y verificación
      de instancias del problema de cobertura de vértices.

    ### Tecnologías utilizadas

    - Python
    - Streamlit
    - NetworkX
    - Plotly
    - Pytest

    ### Propósito académico

    Aplicar conceptos de Teoría de la Computación
    mediante modelos de grafos, algoritmos de exploración,
    problemas de decisión y análisis de complejidad.
    """)

    st.divider()

    st.caption(
        "GraphLab TC · Proyecto universitario · UNAH · 2026"
    )
