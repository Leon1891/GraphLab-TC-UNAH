
"""Controles de edición; la visualización se mantiene fuera del dominio."""

import streamlit as st

from core.grafo import (
    agregar_arista,
    agregar_vertice,
    eliminar_arista,
    eliminar_vertice,
    exportar_json,
    grafo_ejemplo,
    importar_json,
    nuevo_grafo,
)
from utilidades.visualizacion import figura_grafo


def _aplicar(operacion, *args):
    try:
        operacion(st.session_state.grafo, *args)
        st.session_state.mensaje = (
            "success",
            "Cambio guardado correctamente."
        )
        st.rerun()
    except ValueError as exc:
        st.error(str(exc))


def _limpiar_editor():
    """Elimina todos los vértices y aristas del editor."""
    st.session_state.grafo = nuevo_grafo()
    st.session_state.confirmar_limpieza = False
    st.session_state.mensaje = (
        "success",
        "El editor se limpió correctamente. Ya podés crear un grafo nuevo."
    )
    st.rerun()


def mostrar_editor():
    st.header("Editor de grafos dirigidos")
    st.caption(
        "Construí el grafo con vértices y aristas. "
        "El análisis BFS/DFS se integra con el núcleo del proyecto."
    )

    if "grafo" not in st.session_state:
        st.session_state.grafo = nuevo_grafo()

    aviso = st.session_state.pop("mensaje", None)
    if aviso:
        getattr(st, aviso[0])(aviso[1])

    # Métricas del grafo
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Vértices",
        len(st.session_state.grafo["vertices"])
    )
    c2.metric(
        "Aristas",
        len(st.session_state.grafo["aristas"])
    )
    c3.metric("Tipo", "Dirigido")

    panel, visor = st.columns([1, 1.8], gap="large")

    # PANEL DE EDICIÓN
    with panel:
        st.subheader("Agregar elementos")

        # Agregar vértices
        with st.form("form_vertice", clear_on_submit=True):
            nombre = st.text_input(
                "Nombre del vértice",
                placeholder="Ejemplo: A"
            )

            crear = st.form_submit_button(
                "Agregar vértice",
                use_container_width=True
            )

        if crear:
            _aplicar(agregar_vertice, nombre)

        vertices = st.session_state.grafo["vertices"]

        # Agregar aristas
        if len(vertices) >= 2:
            with st.form("form_arista"):
                origen = st.selectbox(
                    "Origen",
                    vertices,
                    key="arista_origen"
                )

                destino = st.selectbox(
                    "Destino",
                    vertices,
                    index=1,
                    key="arista_destino"
                )

                enlazar = st.form_submit_button(
                    "Agregar arista →",
                    use_container_width=True
                )

            if enlazar:
                _aplicar(agregar_arista, origen, destino)

        else:
            st.info(
                "Agregá al menos dos vértices para conectarlos."
            )

        # Eliminar elementos individualmente
        with st.expander("Eliminar elementos"):
            if vertices:
                quitar = st.selectbox(
                    "Eliminar vértice",
                    vertices,
                    key="eliminar_vertice"
                )

                if st.button(
                    "Eliminar vértice",
                    use_container_width=True
                ):
                    _aplicar(eliminar_vertice, quitar)

            else:
                st.info("No hay vértices para eliminar.")

            aristas = st.session_state.grafo["aristas"]

            if aristas:
                opciones = {
                    f"{u} → {v}": (u, v)
                    for u, v in aristas
                }

                eleccion = st.selectbox(
                    "Eliminar arista",
                    list(opciones),
                    key="eliminar_arista"
                )

                if st.button(
                    "Eliminar arista",
                    use_container_width=True
                ):
                    _aplicar(
                        eliminar_arista,
                        *opciones[eleccion]
                    )

            else:
                st.info("No hay aristas para eliminar.")

        # Limpiar todo el editor
        st.divider()
        st.subheader("Limpiar editor")

        if st.button(
            "Limpiar todo el grafo",
            use_container_width=True
        ):
            st.session_state.confirmar_limpieza = True

        if st.session_state.get("confirmar_limpieza", False):
            st.warning(
                "¿Estás segura de que deseas eliminar todos "
                "los vértices y aristas del editor?"
            )

            confirmar, cancelar = st.columns(2)

            with confirmar:
                if st.button(
                    "Sí, limpiar",
                    type="primary",
                    use_container_width=True
                ):
                    _limpiar_editor()

            with cancelar:
                if st.button(
                    "Cancelar",
                    use_container_width=True
                ):
                    st.session_state.confirmar_limpieza = False
                    st.rerun()

    # VISUALIZACIÓN
    with visor:
        st.subheader("Visualización")

        if vertices:
            st.plotly_chart(
                figura_grafo(st.session_state.grafo),
                use_container_width=True,
                config={"displayModeBar": False}
            )
        else:
            st.info(
                "El grafo está vacío. Agregá un vértice "
                "o cargá el ejemplo."
            )

        if st.button(
            "Cargar grafo de ejemplo",
            use_container_width=True
        ):
            st.session_state.grafo = grafo_ejemplo()
            st.session_state.confirmar_limpieza = False
            st.rerun()

    # IMPORTAR Y EXPORTAR
    st.divider()
    st.subheader("Importar y exportar")

    izq, der = st.columns(2)

    with izq:
        st.download_button(
            "Descargar grafo (JSON)",
            data=exportar_json(st.session_state.grafo),
            file_name="graphlab_grafo.json",
            mime="application/json",
            use_container_width=True,
        )

    with der:
        archivo = st.file_uploader(
            "Importar grafo JSON",
            type="json",
            help="El archivo debe tener listas de vertices y aristas."
        )

        if archivo is not None and st.button("Cargar archivo"):
            try:
                st.session_state.grafo = importar_json(
                    archivo.getvalue().decode("utf-8")
                )

                st.session_state.confirmar_limpieza = False
                st.session_state.mensaje = (
                    "success",
                    "Grafo importado correctamente."
                )

                st.rerun()

            except (ValueError, UnicodeDecodeError) as exc:
                st.error(f"No se pudo importar: {exc}")

    # DATOS INTERNOS
    with st.expander("Ver datos del grafo"):
        st.json(st.session_state.grafo)
