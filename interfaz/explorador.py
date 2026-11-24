
"""Explorador visual de GraphLab TC."""

from html import escape

import streamlit as st

from core.grafo import exportar_json, grafo_ejemplo, nuevo_grafo
from utilidades.visualizacion import figura_grafo


ESTILOS = """
<style>
[data-testid="stAppViewContainer"] {
    background: radial-gradient(
        ellipse at 80% 0%, #17254b, #0b1120 38%, #070c17
    );
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101b30, #0b1322);
    border-right: 1px solid #263656;
}

.block-container {
    max-width: 1460px;
    padding-top: 2rem;
}

.gl-hero {
    padding: 28px 32px;
    margin-bottom: 20px;
    border-radius: 20px;
    border: 1px solid #314a72;
    background: linear-gradient(
        115deg, #152951, #111d37 65%, #10283a
    );
    box-shadow: 0 14px 35px rgba(0,0,0,.18);
}

.gl-kicker {
    color: #60e5d0;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
}

.gl-title {
    margin: 10px 0;
    color: #f8fbff;
    font-size: clamp(27px, 3vw, 39px);
    font-weight: 800;
}

.gl-title span {
    color: #76dcec;
}

.gl-subtitle {
    color: #a9bdd9;
    font-size: 14px;
    line-height: 1.65;
    max-width: 750px;
}

.gl-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 16px;
}

.gl-badge {
    display: inline-block;
    border: 1px solid #355377;
    border-radius: 25px;
    padding: 6px 11px;
    background: #1e3455;
    color: #bde9fc;
    font-size: 11px;
    font-weight: 700;
}

.gl-badge.ready {
    color: #8df0cc;
    background: #123d37;
    border-color: #24655a;
}

.gl-card {
    padding: 17px;
    min-height: 106px;
    margin-bottom: 10px;
    border-radius: 15px;
    border: 1px solid #293b57;
    background: linear-gradient(155deg, #16233a, #101a2c);
}

.gl-card-label {
    font-size: 11px;
    color: #8ca6c5;
    font-weight: 800;
    letter-spacing: .6px;
}

.gl-card-number {
    font-size: 29px;
    color: #f8fbff;
    font-weight: 800;
    margin-top: 7px;
}

.gl-card-note {
    color: #6687ae;
    font-size: 11px;
    margin-top: 5px;
}

.gl-section-head {
    color: #ecf7ff;
    font-size: 18px;
    font-weight: 750;
    margin: 8px 0 12px;
}

.gl-legend {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 14px;
    margin: 4px 0 12px;
}

.gl-legend-item {
    color: #b9cde4;
    font-size: 12px;
    display: inline-flex;
    gap: 7px;
    align-items: center;
}

.gl-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    display: inline-block;
}

.gl-result {
    background: #14233b;
    border: 1px solid #2d4d72;
    border-left: 3px solid #52cbd7;
    border-radius: 12px;
    padding: 17px;
}

.gl-route {
    color: #f4f7ff;
    font-weight: 800;
    font-size: 18px;
    margin: 8px 0;
    overflow-wrap: anywhere;
}

.gl-muted {
    color: #95adc9;
    font-size: 12px;
    line-height: 1.5;
}

.stButton > button {
    background: linear-gradient(100deg, #1e568e, #1c7f92);
    border: 1px solid #367f9c;
    color: white;
    border-radius: 10px;
    font-weight: 700;
}

.stButton > button:hover {
    background: #237a91;
    border-color: #73e2da;
    color: white;
}

@media (max-width: 700px) {
    .gl-hero {
        padding: 20px 18px;
    }

    .gl-card {
        padding: 12px;
        min-height: 90px;
    }

    .gl-card-number {
        font-size: 24px;
    }
}
</style>
"""


def tarjeta(titulo, valor, detalle):
    st.html(f"""
    <div class="gl-card">
        <div class="gl-card-label">{escape(str(titulo))}</div>
        <div class="gl-card-number">{escape(str(valor))}</div>
        <div class="gl-card-note">{escape(str(detalle))}</div>
    </div>
    """)


def preparar_figura(grafo, origen, destino, distribucion):
    figura = figura_grafo(grafo, distribucion=distribucion)

    if figura.data:
        nodos = figura.data[-1]

        nombres = (
            list(nodos.text)
            if nodos.text is not None
            else list(grafo["vertices"])
        )

        nodos.marker.size = [
            54 if n in (origen, destino) else 43
            for n in nombres
        ]

        nodos.marker.color = [
            "#2dd4bf" if n == origen else
            "#f59e65" if n == destino else
            "#4e80ed"
            for n in nombres
        ]

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


def mostrar_explorador():
    st.html(ESTILOS)

    st.html("""
    <div class="gl-hero">
        <div class="gl-kicker">
            ISC-312 · GRAPHLAB TC · MÓDULO 02
        </div>

        <div class="gl-title">
            Exploración <span>BFS / DFS</span>
        </div>

        <div class="gl-subtitle">
            Explorá grafos dirigidos, configurá consultas
            de alcanzabilidad y analizá visualmente
            las conexiones entre vértices.
        </div>

        <div class="gl-badges">
            <span class="gl-badge ready">
                ● Visualizador activo
            </span>
            <span class="gl-badge">
                Grafo dirigido
            </span>
            <span class="gl-badge">
                Algoritmos pendientes de integración
            </span>
        </div>
    </div>
    """)

    if "grafo" not in st.session_state:
        st.session_state.grafo = nuevo_grafo()

    grafo = st.session_state.grafo
    vertices = list(grafo["vertices"])
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

            algoritmo = st.selectbox(
                "Algoritmo",
                ["BFS", "DFS"],
                key="explorador_algoritmo"
            )

            st.subheader("Opciones visuales")

            distribuciones = {
                "Automática": "auto",
                "Jerárquica": "jerarquica",
                "Orgánica": "organica",
                "Circular": "circular"
            }

            nombre_distribucion = st.selectbox(
                "Distribución de nodos",
                list(distribuciones),
                key="explorador_distribucion"
            )

            zoom = st.toggle(
                "Zoom con rueda del mouse",
                value=False,
                key="explorador_zoom"
            )

            st.caption(
                "La ejecución de BFS y DFS se integrará "
                "cuando Dinora entregue los algoritmos."
            )

            if st.button(
                "Restablecer grafo de ejemplo",
                use_container_width=True
            ):
                st.session_state.grafo = grafo_ejemplo()
                st.rerun()

        st.html(
            '<div class="gl-section-head">'
            'Consulta preparada</div>'
        )

        st.html(f"""
        <div class="gl-result">
            <div class="gl-kicker">
                {escape(algoritmo)} · ALCANZABILIDAD
            </div>

            <div class="gl-route">
                {escape(origen)} &rarr; {escape(destino)}
            </div>

            <div class="gl-muted">
                El origen se muestra en verde y
                el destino en naranja.
                La búsqueda todavía no se ha ejecutado.
            </div>
        </div>
        """)

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
                distribuciones[nombre_distribucion]
            )

            st.plotly_chart(
                figura,
                width="stretch",
                key="explorador_grafo_plot",
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

        with st.expander("Ver estructura del grafo"):
            st.json(grafo)

    st.caption(
        "GraphLab TC · UNAH · Visualización en desarrollo"
    )
