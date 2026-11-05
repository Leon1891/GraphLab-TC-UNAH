"""Punto de entrada de GraphLab TC."""

import streamlit as st

from interfaz.editor import mostrar_editor
from interfaz.explorador import mostrar_explorador

st.set_page_config(
    page_title="GraphLab TC | UNAH",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded",
)

with st.sidebar:
    st.title("🕸️ GraphLab TC")
    st.caption("ISC-312 · Teoría de la Computación | UNAH")
    pagina = st.radio(
        "Navegación",
        ["Editor de grafos", "Exploración BFS/DFS", "Comparación", "Vertex Cover", "Acerca del proyecto"],
    )
    st.divider()
    st.caption("Versión inicial 0.1.0 · Entorno de desarrollo")

if pagina == "Editor de grafos":
    mostrar_editor()
elif pagina == "Exploración BFS/DFS":
    mostrar_explorador()
elif pagina == "Comparación":
    st.header("Comparación de algoritmos")
    st.info("Módulo planificado: recorridos, tiempos, memoria y complejidad teórica.")
elif pagina == "Vertex Cover":
    st.header("Problema de decisión: Vertex Cover")
    st.info("Módulo planificado: búsqueda exacta y verificación de cobertura para grafos pequeños.")
else:
    st.title("Acerca de GraphLab TC")
    st.write("Proyecto universitario #6 · Explorador de grafos, alcanzabilidad y problemas de decisión.")
    st.write("Dos desarrolladores: lógica y algoritmos; interfaz, visualización e integración.")
    st.caption("El software se mantiene modular para incluir fundamentos y pruebas documentadas.")
