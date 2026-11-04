"""Visualización dirigida usando NetworkX únicamente como ayuda gráfica."""

import math

import networkx as nx
import plotly.graph_objects as go


def figura_grafo(grafo):
    g = nx.DiGraph()
    g.add_nodes_from(grafo["vertices"])
    g.add_edges_from(tuple(arista) for arista in grafo["aristas"])
    posiciones = nx.spring_layout(g, seed=42) if g.number_of_nodes() > 1 else {n: (0.0, 0.0) for n in g.nodes}
    fig = go.Figure()

    # Cada arista se dibuja como flecha; el extremo se separa del círculo del nodo.
    for origen, destino in g.edges:
        x0, y0 = posiciones[origen]
        x1, y1 = posiciones[destino]
        dx, dy = x1 - x0, y1 - y0
        d = math.hypot(dx, dy) or 1.0
        margen = min(0.12, d * 0.22)
        fig.add_annotation(
            x=x1 - dx * margen / d, y=y1 - dy * margen / d,
            ax=x0 + dx * margen / d, ay=y0 + dy * margen / d,
            xref="x", yref="y", axref="x", ayref="y",
            text="", showarrow=True, arrowhead=2, arrowsize=1.3,
            arrowwidth=1.9, arrowcolor="#7890AA",
        )

    fig.add_trace(go.Scatter(
        x=[posiciones[n][0] for n in g.nodes],
        y=[posiciones[n][1] for n in g.nodes],
        mode="markers+text", text=list(g.nodes), textposition="middle center",
        textfont=dict(color="white", size=14),
        marker=dict(size=42, color="#2766C3", line=dict(width=2, color="#B6D7FF")),
        hoverinfo="text", hovertext=[f"Vértice: {n}" for n in g.nodes],
        showlegend=False,
    ))
    fig.update_layout(
        template="plotly_white", margin=dict(l=12, r=12, t=12, b=12),
        height=460, plot_bgcolor="#F5F8FD", paper_bgcolor="#F5F8FD",
        xaxis=dict(visible=False, range=[-1.35, 1.35], scaleanchor="y"),
        yaxis=dict(visible=False, range=[-1.3, 1.3]),
    )
    return fig
