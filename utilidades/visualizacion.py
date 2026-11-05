"""Visualizador interactivo de grafos de GraphLab TC.

Responsabilidad del Desarrollador 2. No implementa ni ejecuta BFS/DFS.
Mantiene la API existente: figura_grafo(grafo) -> plotly.graph_objects.Figure.
"""

import math

import networkx as nx
import plotly.graph_objects as go


FONDO = "#0E192C"
ARISTA = "#8AA9CF"
ACENTO = "#70C9FF"


def _posiciones(grafo, distribucion):
    """Calcula posiciones estables y legibles, sin alterar el grafo recibido."""
    total = grafo.number_of_nodes()
    if total == 0:
        return {}
    if total == 1:
        return {next(iter(grafo.nodes)): (0.0, 0.0)}

    if distribucion == "auto":
        distribucion = "jerarquica" if nx.is_directed_acyclic_graph(grafo) and total <= 28 else "organica"

    if distribucion == "jerarquica":
        if nx.is_directed_acyclic_graph(grafo):
            niveles = [sorted(nivel, key=str) for nivel in nx.topological_generations(grafo)]
            numero_niveles = len(niveles)
            posiciones = {}
            for indice, nivel in enumerate(niveles):
                x = -1.13 + 2.26 * indice / max(1, numero_niveles - 1)
                for fila, nodo in enumerate(nivel):
                    # Se distribuyen los nodos del mismo nivel sin amontonarlos.
                    y = 0.0 if len(nivel) == 1 else 0.98 - 1.96 * fila / (len(nivel) - 1)
                    posiciones[nodo] = (x, y)
            return posiciones
        distribucion = "organica"  # Los grafos con ciclos no tienen orden topológico.

    if distribucion == "circular":
        lista = sorted(grafo.nodes, key=str)
        return {
            nodo: (1.0 * math.cos(2 * math.pi * i / total),
                   1.0 * math.sin(2 * math.pi * i / total))
            for i, nodo in enumerate(lista)
        }

    if distribucion not in {"organica", "auto"}:
        raise ValueError("Distribución no admitida. Usá auto, jerarquica, organica o circular.")

    # Semilla fija: la distribución no salta al cambiar de página.
    pos = nx.spring_layout(grafo, seed=42, iterations=140, k=1.3 / math.sqrt(total))
    return {n: (float(p[0]), float(p[1])) for n, p in pos.items()}


def _arista(figura, origen, destino, posiciones, es_bidireccional):
    """Dibuja una flecha cuyo extremo no queda oculto dentro del nodo."""
    x0, y0 = posiciones[origen]
    x1, y1 = posiciones[destino]
    dx, dy = x1 - x0, y1 - y0
    distancia = math.hypot(dx, dy)
    if distancia < 1e-6:
        return

    ux, uy = dx / distancia, dy / distancia
    # Ajuste pequeño para no tapar el borde de los círculos.
    margen = min(0.135, distancia * 0.23)
    inicio = (x0 + ux * margen, y0 + uy * margen)
    fin = (x1 - ux * margen, y1 - uy * margen)

    if es_bidireccional:
        # Las direcciones opuestas siguen curvas distintas.
        normal_x, normal_y = -uy, ux
        curvatura = min(0.18, distancia * 0.17)
        control = ((inicio[0] + fin[0]) / 2 + normal_x * curvatura,
                   (inicio[1] + fin[1]) / 2 + normal_y * curvatura)
        puntos = []
        for i in range(17):
            t = i / 16
            x = (1 - t) ** 2 * inicio[0] + 2 * (1 - t) * t * control[0] + t * t * fin[0]
            y = (1 - t) ** 2 * inicio[1] + 2 * (1 - t) * t * control[1] + t * t * fin[1]
            puntos.append((x, y))
        figura.add_trace(go.Scatter(
            x=[p[0] for p in puntos], y=[p[1] for p in puntos],
            mode="lines", line=dict(color=ARISTA, width=2.1),
            hoverinfo="skip", showlegend=False,
        ))
        # Flecha corta tangente a la curva, evitando una segunda línea recta.
        inicio_flecha = puntos[-3]
    else:
        # Las aristas simples también llevan flecha, no solo una línea sin dirección.
        inicio_flecha = inicio

    figura.add_annotation(
        x=fin[0], y=fin[1], ax=inicio_flecha[0], ay=inicio_flecha[1],
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True, text="", arrowhead=2, arrowsize=1.35,
        arrowwidth=2.1, arrowcolor=ARISTA,
    )


def figura_grafo(grafo, distribucion="auto"):
    """Devuelve el grafo en Plotly. No altera vértices ni aristas.

    distribucion: 'auto' | 'jerarquica' | 'organica' | 'circular'.
    La última traza contiene los nodos, por compatibilidad con explorador.py.
    """
    red = nx.DiGraph()
    red.add_nodes_from(grafo["vertices"])
    red.add_edges_from(tuple(arista) for arista in grafo["aristas"])
    posiciones = _posiciones(red, distribucion)
    figura = go.Figure()

    # Cuadrícula fina: guía visual, sin competir con las conexiones.
    for coordenada in (-1.0, -0.5, 0.0, 0.5, 1.0):
        figura.add_shape(type="line", x0=coordenada, x1=coordenada,
                         y0=-1.27, y1=1.27,
                         line=dict(color="rgba(115,147,187,0.055)", width=1),
                         layer="below")
        figura.add_shape(type="line", x0=-1.31, x1=1.31,
                         y0=coordenada, y1=coordenada,
                         line=dict(color="rgba(115,147,187,0.055)", width=1),
                         layer="below")

    for origen, destino in red.edges:
        _arista(figura, origen, destino, posiciones, red.has_edge(destino, origen))

    nodos = list(red.nodes)
    if nodos:
        xs = [posiciones[n][0] for n in nodos]
        ys = [posiciones[n][1] for n in nodos]
        # Aureola de luz suave. La última traza seguirá siendo la de los nodos.
        figura.add_trace(go.Scatter(
            x=xs, y=ys, mode="markers",
            marker=dict(size=66, color="rgba(61,144,255,0.12)"),
            hoverinfo="skip", showlegend=False,
        ))
        figura.add_trace(go.Scatter(
            x=xs, y=ys, mode="markers+text",
            text=nodos, textposition="middle center",
            textfont=dict(color="#FFFFFF", size=15, family="Arial Black"),
            marker=dict(size=46, color="#326FD7",
                        line=dict(width=2.5, color="#A5CEFF")),
            customdata=[[red.in_degree(n), red.out_degree(n)] for n in nodos],
            hovertemplate=("<b>Vértice %{text}</b><br>Entrantes: %{customdata[0]}"
                           "<br>Salientes: %{customdata[1]}<extra></extra>"),
            showlegend=False,
        ))

    figura.update_layout(
        template="plotly_dark", height=520,
        paper_bgcolor=FONDO, plot_bgcolor=FONDO,
        margin=dict(l=14, r=14, t=20, b=14),
        font=dict(color="#ECF5FF"),
        hoverlabel=dict(bgcolor="#1B3353", font_color="#FFFFFF", bordercolor="#41658C"),
        xaxis=dict(visible=False, range=[-1.38, 1.38], fixedrange=False),
        yaxis=dict(visible=False, range=[-1.39, 1.39], scaleanchor="x", scaleratio=1,
                   fixedrange=False),
        showlegend=False,
    )
    return figura
