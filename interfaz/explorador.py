
"""Explorador visual de GraphLab TC."""

from pathlib import Path
from html import escape

import streamlit as st

from core.grafo import exportar_json, grafo_ejemplo, nuevo_grafo
from algoritmos.bfs import bfs
from algoritmos.dfs import dfs
from algoritmos.vertex_cover import (
    resolver_vertex_cover,
    verificar_cobertura,
)
from utilidades.visualizacion import figura_grafo


MAX_VERTICES_VERTEX_COVER = 16


def firma_grafo(grafo):
    """Genera una firma para detectar cambios en el grafo."""

    return (
        tuple(grafo["vertices"]),
        tuple(tuple(arista) for arista in grafo["aristas"]),
    )


def cargar_estilos():
    """Carga los estilos externos del explorador."""

    ruta_css = (
        Path(__file__).resolve().parent.parent
        / "estilos"
        / "explorador.css"
    )

    with open(ruta_css, encoding="utf-8") as archivo:
        st.html(f"<style>{archivo.read()}</style>")


def tarjeta(titulo, valor, detalle):
    """Muestra una tarjeta de información."""

    st.html(f"""
    <div class="gl-card">
        <div class="gl-card-label">{escape(str(titulo))}</div>
        <div class="gl-card-number">{escape(str(valor))}</div>
        <div class="gl-card-note">{escape(str(detalle))}</div>
    </div>
    """)


def mostrar_metricas(grafo):
    """Muestra las métricas generales del grafo."""

    vertices = grafo["vertices"]
    aristas = grafo["aristas"]
    cantidad = len(vertices)

    densidad = (
        100 * len(aristas) / (cantidad * (cantidad - 1))
        if cantidad > 1 else 0
    )

    metricas = [
        ("VÉRTICES", cantidad, "Nodos registrados"),
        ("ARISTAS", len(aristas), "Conexiones dirigidas"),
        ("DENSIDAD", f"{densidad:.0f}%", "De las conexiones posibles"),
        (
            "ESTADO",
            "Listo" if cantidad else "Vacío",
            "Editor sincronizado"
        )
    ]

    columnas = st.columns(4)

    for columna, datos in zip(columnas, metricas):
        with columna:
            tarjeta(*datos)


def preparar_figura(
    grafo,
    origen=None,
    destino=None,
    distribucion="auto",
    cobertura=None
):
    """Prepara el gráfico y resalta los vértices importantes."""

    figura = figura_grafo(
        grafo,
        distribucion=distribucion
    )

    cobertura = set(cobertura or [])

    if figura.data:
        nodos = figura.data[-1]

        nombres = (
            list(nodos.text)
            if nodos.text is not None
            else list(grafo["vertices"])
        )

        colores = []
        tamanos = []

        for nombre in nombres:

            if nombre in cobertura:
                colores.append("#a78bfa")
                tamanos.append(56)

            elif nombre == origen:
                colores.append("#2dd4bf")
                tamanos.append(54)

            elif nombre == destino:
                colores.append("#f59e65")
                tamanos.append(54)

            else:
                colores.append("#4e80ed")
                tamanos.append(43)

        nodos.marker.size = tamanos
        nodos.marker.color = colores

        nodos.marker.line = dict(
            color="#dce9ff",
            width=2.5
        )

        nodos.textfont = dict(
            color="#ffffff",
            size=15,
            family="Arial Black"
        )

    for flecha in figura.layout.annotations or []:
        flecha.arrowcolor = "#819abf"
        flecha.arrowwidth = 2

    figura.update_layout(
        template="plotly_dark",
        height=515,
        margin=dict(l=6, r=6, t=15, b=8),
        paper_bgcolor="#0e192c",
        plot_bgcolor="#0e192c",
        font=dict(color="#dfedff"),
        hoverlabel=dict(
            bgcolor="#1e3555",
            font_color="#ffffff"
        ),
        showlegend=False
    )

    figura.update_xaxes(
        showgrid=False,
        zeroline=False,
        showticklabels=False
    )

    figura.update_yaxes(
        showgrid=False,
        zeroline=False,
        showticklabels=False
    )

    return figura


def mostrar_opciones_visuales(prefijo):
    """Presenta las opciones de distribución y zoom."""

    distribuciones = {
        "Automática": "auto",
        "Jerárquica": "jerarquica",
        "Orgánica": "organica",
        "Circular": "circular"
    }

    nombre_distribucion = st.selectbox(
        "Distribución de nodos",
        list(distribuciones),
        key=f"{prefijo}_distribucion"
    )

    zoom = st.toggle(
        "Zoom con rueda del mouse",
        value=False,
        key=f"{prefijo}_zoom"
    )

    return distribuciones[nombre_distribucion], nombre_distribucion, zoom


def mostrar_grafico(
    grafo,
    distribucion,
    nombre_distribucion,
    zoom,
    key,
    origen=None,
    destino=None,
    cobertura=None
):
    """Muestra el grafo y su leyenda."""

    if cobertura is not None:
        st.html("""
        <div class="gl-legend">
            <span class="gl-legend-item">
                <span class="gl-dot"
                      style="background:#a78bfa"></span>
                Vértices seleccionados
            </span>

            <span class="gl-legend-item">
                <span class="gl-dot"
                      style="background:#4e80ed"></span>
                Otros vértices
            </span>
        </div>
        """)
    else:
        st.html("""
        <div class="gl-legend">
            <span class="gl-legend-item">
                <span class="gl-dot"
                      style="background:#2dd4bf"></span>
                Origen
            </span>

            <span class="gl-legend-item">
                <span class="gl-dot"
                      style="background:#f59e65"></span>
                Destino
            </span>

            <span class="gl-legend-item">
                <span class="gl-dot"
                      style="background:#4e80ed"></span>
                Otros vértices
            </span>
        </div>
        """)

    with st.container(border=True):

        figura = preparar_figura(
            grafo,
            origen,
            destino,
            distribucion,
            cobertura
        )

        st.plotly_chart(
            figura,
            width="stretch",
            key=key,
            config={
                "displayModeBar": True,
                "displaylogo": False,
                "scrollZoom": zoom,
                "modeBarButtonsToRemove": [
                    "lasso2d",
                    "select2d",
                    "autoScale2d"
                ]
            }
        )

        st.caption(
            f"Distribución: {nombre_distribucion}. "
            "Usá las herramientas del gráfico para "
            "acercar, alejar y restablecer la vista."
        )


def mostrar_estructura_grafo(grafo):
    """Permite consultar la estructura interna del grafo."""

    with st.expander("Ver estructura del grafo"):
        st.json(grafo)


def mostrar_resultado(
    consulta,
    algoritmo,
    origen,
    destino,
    grafo
):
    """Muestra los resultados de BFS o DFS si siguen vigentes."""

    if not consulta:
        st.info(
            "Configurá los parámetros y presioná Ejecutar "
            "para analizar el grafo."
        )
        return

    if consulta.get("firma_grafo") != firma_grafo(grafo):
        st.info(
            "El grafo cambió desde la última búsqueda. "
            "Ejecutá nuevamente el algoritmo."
        )
        return

    if consulta["algoritmo"] != algoritmo:
        st.info(
            "La configuración cambió. "
            "Ejecutá nuevamente el algoritmo."
        )
        return

    if (
        consulta["origen"] != origen
        or consulta["destino"] != destino
    ):
        st.info(
            "La configuración cambió. "
            "Presioná Ejecutar para realizar una nueva búsqueda."
        )
        return

    resultado = consulta["resultado"]

    if resultado["alcanzable"]:
        st.success("¡Se encontró una ruta!")

        ruta = " → ".join(resultado["ruta"])

        st.html(f"""
        <div class="gl-result">
            <div class="gl-kicker">
                {escape(algoritmo)} · RUTA ENCONTRADA
            </div>
            <div class="gl-route">
                {escape(ruta)}
            </div>
            <div class="gl-muted">
                Se encontró un camino desde
                {escape(origen)} hasta {escape(destino)}.
            </div>
        </div>
        """)
    else:
        st.warning(
            f"No existe una ruta desde {origen} hasta {destino}."
        )

    columna1, columna2 = st.columns(2)

    with columna1:
        st.metric(
            "Vértices procesados",
            len(resultado["visitados"])
        )

    with columna2:
        st.metric(
            "Pasos de exploración",
            len(resultado["pasos"])
        )

    st.markdown("**Vértices visitados**")

    st.write(
        " → ".join(resultado["visitados"])
        if resultado["visitados"]
        else "Ninguno"
    )

    with st.expander("Ver pasos de la exploración"):
        for numero, paso in enumerate(resultado["pasos"], start=1):
            st.markdown(
                f"**Paso {numero}: vértice {paso['actual']}**"
            )

            st.write("Frontera:", paso["frontera"])
            st.write("Visitados:", paso["visitados"])


def mostrar_resultado_vertex_cover(consulta, k, grafo):
    """Muestra y verifica el resultado vigente de Vertex Cover."""

    if not consulta:
        st.info(
            "Configurá el valor de K y presioná "
            "Ejecutar Vertex Cover."
        )
        return

    if consulta.get("firma_grafo") != firma_grafo(grafo):
        st.info(
            "El grafo cambió desde el último análisis. "
            "Ejecutá nuevamente Vertex Cover."
        )
        return

    if consulta["k"] != k:
        st.info(
            "El valor de K cambió. "
            "Ejecutá nuevamente Vertex Cover."
        )
        return

    resultado = consulta["resultado"]

    st.markdown(f"**Límite de cobertura: K = {k}**")

    if resultado["existe"]:

        cobertura = resultado["cobertura"]

        valida = verificar_cobertura(grafo, cobertura, k)

        if not valida:
            st.error(
                "La solución encontrada no superó la verificación."
            )
            return

        st.success(
            "¡Se encontró una cobertura de vértices válida!"
        )

        st.html(f"""
        <div class="gl-result">
            <div class="gl-kicker">
                VERTEX COVER · SOLUCIÓN ENCONTRADA
            </div>
            <div class="gl-route">
                {escape(" , ".join(cobertura) if cobertura else "Sin vértices")}
            </div>
            <div class="gl-muted">
                Todos los extremos de las aristas están cubiertos
                por al menos un vértice seleccionado.
            </div>
        </div>
        """)

        columna1, columna2 = st.columns(2)

        with columna1:
            st.metric("Vértices seleccionados", len(cobertura))

        with columna2:
            st.metric("Aristas cubiertas", len(grafo["aristas"]))

        st.markdown("**Verificación de la solución**")

        for a, b in grafo["aristas"]:
            if a in cobertura or b in cobertura:
                st.write(f"✓ {a} — {b}: cubierta")
            else:
                st.error(f"✗ {a} — {b}: no cubierta")

        st.caption(
            "El algoritmo busca primero las combinaciones "
            "más pequeñas. Por eso encuentra una cobertura "
            "mínima dentro del límite establecido."
        )

    else:
        st.warning(
            f"No existe una cobertura de vértices "
            f"con un máximo de {k} vértices."
        )

        st.caption("Probá aumentando el valor de K.")


def mostrar_explorador():
    """Presenta la pantalla de exploración BFS y DFS."""

    cargar_estilos()

    st.html("""
    <div class="gl-hero">
        <div class="gl-kicker">
            ISC-312 · GRAPHLAB TC · MÓDULO 02
        </div>

        <div class="gl-title">
            Exploración <span>de grafos</span>
        </div>

        <div class="gl-subtitle">
            Explorá grafos dirigidos, configurá consultas
            de alcanzabilidad y analizá rutas mediante
            los algoritmos BFS y DFS.
        </div>

        <div class="gl-badges">
            <span class="gl-badge ready">
                ● Visualizador activo
            </span>
            <span class="gl-badge">
                Grafo dirigido
            </span>
            <span class="gl-badge ready">
                BFS y DFS integrados
            </span>
        </div>
    </div>
    """)

    if "grafo" not in st.session_state:
        st.session_state.grafo = nuevo_grafo()

    grafo = st.session_state.grafo
    vertices = list(grafo["vertices"])

    mostrar_metricas(grafo)

    if not vertices:
        st.info(
            "El grafo está vacío. Podés cargar el ejemplo "
            "o crear nodos desde Editor de grafos."
        )

        if st.button(
            "Cargar grafo de ejemplo",
            key="explorador_cargar_ejemplo"
        ):
            st.session_state.grafo = grafo_ejemplo()
            st.session_state.pop("explorador_resultado", None)
            st.rerun()

        return

    izquierda, derecha = st.columns(
        [1.85, 1],
        gap="large"
    )

    with derecha:
        st.html(
            '<div class="gl-section-head">Panel de control</div>'
        )

        with st.container(border=True):
            st.caption("CONFIGURACIÓN DE CONSULTA")

            algoritmo = st.selectbox(
                "Algoritmo",
                ["BFS", "DFS"],
                key="explorador_algoritmo"
            )

            origen = st.selectbox(
                "Vértice de origen",
                vertices,
                key="explorador_origen"
            )

            destino = st.selectbox(
                "Vértice de destino",
                vertices,
                index=len(vertices) - 1,
                key="explorador_destino"
            )

            st.subheader("Opciones visuales")

            distribucion, nombre_distribucion, zoom = (
                mostrar_opciones_visuales("explorador")
            )

            if st.button(
                f"Ejecutar {algoritmo}",
                use_container_width=True,
                type="primary",
                key="ejecutar_exploracion"
            ):
                try:
                    if algoritmo == "BFS":
                        resultado = bfs(grafo, origen, destino)
                    else:
                        resultado = dfs(grafo, origen, destino)

                    st.session_state["explorador_resultado"] = {
                        "algoritmo": algoritmo,
                        "origen": origen,
                        "destino": destino,
                        "firma_grafo": firma_grafo(grafo),
                        "resultado": resultado
                    }

                except ValueError as error:
                    st.session_state.pop(
                        "explorador_resultado",
                        None
                    )
                    st.error(str(error))

            if st.button(
                "Restablecer grafo de ejemplo",
                use_container_width=True,
                key="explorador_restaurar"
            ):
                st.session_state.grafo = grafo_ejemplo()
                st.session_state.pop(
                    "explorador_resultado",
                    None
                )
                st.rerun()

        st.html(
            '<div class="gl-section-head">'
            'Resultado de la consulta</div>'
        )

        consulta = st.session_state.get(
            "explorador_resultado"
        )

        mostrar_resultado(
            consulta,
            algoritmo,
            origen,
            destino,
            grafo
        )

        st.download_button(
            "Exportar grafo JSON",
            data=exportar_json(grafo),
            file_name="graphlab_grafo.json",
            mime="application/json",
            use_container_width=True
        )

    with izquierda:
        st.html(
            '<div class="gl-section-head">'
            'Mapa interactivo del grafo</div>'
        )

        consulta = st.session_state.get(
            "explorador_resultado"
        )

        origen_grafico = None
        destino_grafico = None

        if (
            consulta
            and consulta.get("firma_grafo") == firma_grafo(grafo)
            and consulta["algoritmo"] == algoritmo
            and consulta["origen"] == origen
            and consulta["destino"] == destino
        ):
            origen_grafico = origen
            destino_grafico = destino

        mostrar_grafico(
            grafo,
            distribucion,
            nombre_distribucion,
            zoom,
            "explorador_grafo_plot",
            origen_grafico,
            destino_grafico
        )

        mostrar_estructura_grafo(grafo)

    st.caption(
        "GraphLab TC · UNAH · Exploración de alcanzabilidad "
        "mediante BFS y DFS"
    )


def mostrar_vertex_cover():
    """Presenta la pantalla independiente de Vertex Cover."""

    cargar_estilos()

    st.html("""
    <div class="gl-hero">
        <div class="gl-kicker">
            ISC-312 · GRAPHLAB TC · MÓDULO 03
        </div>

        <div class="gl-title">
            Problema de <span>Vertex Cover</span>
        </div>

        <div class="gl-subtitle">
            Analizá si existe un conjunto de vértices
            que cubra todas las aristas del grafo
            sin superar el límite K establecido.
        </div>

        <div class="gl-badges">
            <span class="gl-badge ready">
                ● Algoritmo integrado
            </span>
            <span class="gl-badge">
                Problema de decisión
            </span>
            <span class="gl-badge ready">
                Verificación de cobertura
            </span>
        </div>
    </div>
    """)

    if "grafo" not in st.session_state:
        st.session_state.grafo = nuevo_grafo()

    grafo = st.session_state.grafo

    mostrar_metricas(grafo)

    vertices = list(grafo["vertices"])

    if not vertices:
        st.info(
            "El grafo está vacío. Podés cargar el ejemplo "
            "o crear nodos desde Editor de grafos."
        )

        if st.button(
            "Cargar grafo de ejemplo",
            key="vertex_cover_cargar_ejemplo"
        ):
            st.session_state.grafo = grafo_ejemplo()
            st.session_state.pop("vertex_cover_resultado", None)
            st.rerun()

        return

    izquierda, derecha = st.columns(
        [1.85, 1],
        gap="large"
    )

    with derecha:
        st.html(
            '<div class="gl-section-head">Panel de control</div>'
        )

        with st.container(border=True):
            st.caption("CONFIGURACIÓN DEL PROBLEMA")

            k = st.number_input(
                "Cantidad máxima de vértices (K)",
                min_value=0,
                max_value=MAX_VERTICES_VERTEX_COVER,
                value=2,
                step=1,
                key="vertex_cover_k"
            )

            st.caption(
                "Vertex Cover busca una selección de hasta K "
                "vértices que cubra todas las aristas."
            )

            st.caption(
                f"Esta versión admite hasta "
                f"{MAX_VERTICES_VERTEX_COVER} vértices "
                "para la búsqueda exacta."
            )

            if len(vertices) > MAX_VERTICES_VERTEX_COVER:
                st.warning(
                    f"El grafo tiene {len(vertices)} vértices. "
                    f"Vertex Cover admite como máximo "
                    f"{MAX_VERTICES_VERTEX_COVER}. "
                    "Reducí el grafo para ejecutar este análisis."
                )

            st.subheader("Opciones visuales")

            distribucion, nombre_distribucion, zoom = (
                mostrar_opciones_visuales("vertex_cover")
            )

            if st.button(
                "Ejecutar Vertex Cover",
                use_container_width=True,
                type="primary",
                key="ejecutar_vertex_cover",
                disabled=len(vertices) > MAX_VERTICES_VERTEX_COVER
            ):
                try:
                    resultado = resolver_vertex_cover(
                        grafo,
                        int(k)
                    )

                    st.session_state["vertex_cover_resultado"] = {
                        "k": int(k),
                        "firma_grafo": firma_grafo(grafo),
                        "resultado": resultado
                    }

                except ValueError as error:
                    st.session_state.pop(
                        "vertex_cover_resultado",
                        None
                    )
                    st.error(str(error))

            if st.button(
                "Restablecer grafo de ejemplo",
                use_container_width=True,
                key="vertex_cover_restaurar"
            ):
                st.session_state.grafo = grafo_ejemplo()
                st.session_state.pop(
                    "vertex_cover_resultado",
                    None
                )
                st.rerun()

        st.html(
            '<div class="gl-section-head">'
            'Resultado de Vertex Cover</div>'
        )

        consulta = st.session_state.get(
            "vertex_cover_resultado"
        )

        mostrar_resultado_vertex_cover(
            consulta,
            int(k),
            grafo
        )

        st.download_button(
            "Exportar grafo JSON",
            data=exportar_json(grafo),
            file_name="graphlab_grafo.json",
            mime="application/json",
            use_container_width=True,
            key="vertex_cover_exportar"
        )

    with izquierda:
        st.html(
            '<div class="gl-section-head">'
            'Visualización de la cobertura</div>'
        )

        consulta = st.session_state.get(
            "vertex_cover_resultado"
        )

        cobertura = []

        if (
            consulta
            and consulta.get("firma_grafo") == firma_grafo(grafo)
            and consulta["k"] == int(k)
            and consulta["resultado"]["existe"]
        ):
            cobertura = consulta["resultado"]["cobertura"]

        mostrar_grafico(
            grafo,
            distribucion,
            nombre_distribucion,
            zoom,
            "vertex_cover_grafo_plot",
            cobertura=cobertura
        )

        mostrar_estructura_grafo(grafo)

    st.caption(
        "GraphLab TC · UNAH · Problema de decisión Vertex Cover"
    )
