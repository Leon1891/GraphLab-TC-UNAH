# GraphLab TC — UNAH

**Proyecto #6 de ISC-312: Teoría de la Computación**

Explorador de grafos, alcanzabilidad y problemas de decisión.

GraphLab TC es una aplicación educativa desarrollada en Python y Streamlit que permite crear, visualizar y explorar grafos dirigidos, estudiar la alcanzabilidad mediante BFS y DFS, comparar algoritmos de recorrido y resolver instancias pequeñas del problema Vertex Cover.

## Estado actual

**Versión de desarrollo: 0.2.0**

El proyecto cuenta con las siguientes funcionalidades implementadas:

- Editor de grafos dirigidos.
- Creación y eliminación de vértices y aristas.
- Validación de las operaciones realizadas sobre los grafos.
- Visualización interactiva de grafos.
- Importación y exportación de grafos en formato JSON.
- Exploración de grafos mediante BFS (búsqueda en anchura).
- Exploración de grafos mediante DFS (búsqueda en profundidad).
- Identificación de alcanzabilidad y recuperación de rutas.
- Registro de vértices visitados y pasos de exploración.
- Comparación de los algoritmos BFS y DFS.
- Resolución de instancias pequeñas del problema Vertex Cover.
- Verificación de coberturas de vértices.
- Pruebas automatizadas con Pytest.

**Resultado de pruebas registrado:** 48 pruebas aprobadas, sin fallos, en la ejecución realizada el 25 de noviembre de 2026.

## Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python | Lenguaje principal |
| Streamlit | Interfaz interactiva |
| NetworkX | Apoyo en el manejo de grafos |
| Plotly | Visualización interactiva |
| Pytest | Pruebas automatizadas |
| JSON | Almacenamiento e intercambio de grafos |
| Git y GitHub | Control de versiones |

## Requisitos

- Python 3.11 o superior.
- Git instalado.
- Visual Studio Code o cualquier editor compatible.
- Conexión a Internet para instalar las dependencias.

## Ejecutar en Windows (PowerShell en VS Code)

Clonar el repositorio y acceder a la carpeta del proyecto.

Crear el entorno virtual:

```powershell
py -3 -m venv .venv
```

Instalar las dependencias:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Iniciar la aplicación:

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

Abrir la dirección local indicada en la terminal, normalmente:

`http://localhost:8501`

## Ejecutar pruebas

Para ejecutar la suite de pruebas automatizadas:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Funcionalidades principales

### 1. Editor de grafos

Permite crear y modificar grafos dirigidos mediante operaciones de administración de vértices y aristas.

Incluye validaciones para evitar operaciones incorrectas y permite importar o exportar grafos utilizando archivos JSON.

### 2. Exploración BFS y DFS

Implementa dos algoritmos fundamentales de recorrido:

- **BFS:** explora los vértices por niveles y encuentra rutas con el menor número de aristas en grafos no ponderados.
- **DFS:** explora una rama del grafo en profundidad antes de continuar con otras alternativas.

Ambos algoritmos permiten analizar la alcanzabilidad entre un vértice de origen y uno de destino.

### 3. Comparación de algoritmos

Presenta los resultados de BFS y DFS y permite estudiar sus diferencias en cuanto a estrategia de exploración, resultados y complejidad teórica.

La complejidad temporal de ambos algoritmos, utilizando listas de adyacencia, es O(V + E).

### 4. Problema Vertex Cover

Permite estudiar el problema de cobertura de vértices en grafos no dirigidos.

El sistema busca una cobertura de tamaño máximo `k` y permite verificar si un conjunto de vértices cubre todas las aristas.

La búsqueda exacta está limitada a grafos de hasta 16 vértices debido al crecimiento exponencial de las posibilidades que deben analizarse.

## Estructura del proyecto

```text
GraphLab-TC-UNAH/
│
├── algoritmos/
│   ├── bfs.py
│   ├── dfs.py
│   └── vertex_cover.py
│
├── core/
│   └── grafo.py
│
├── docs/
│
├── ejemplos/
│   └── grafo_ejemplo.json
│
├── estilos/
│   └── explorador.css
│
├── interfaz/
│   ├── comparacion.py
│   ├── editor.py
│   └── explorador.py
│
├── tests/
│   ├── test_bfs.py
│   ├── test_dfs.py
│   ├── test_grafo.py
│   └── test_vertex_cover.py
│
├── utilidades/
│   └── visualizacion.py
│
├── streamlit_app.py
└── requirements.txt
```

## Documentación académica

El proyecto incluye documentación relacionada con los fundamentos de Teoría de la Computación, la arquitectura del sistema y las pruebas.

Entre los temas abordados se encuentran:

- Conjuntos, alfabetos, cadenas y lenguajes formales.
- Relaciones y funciones.
- Autómatas finitos deterministas y no deterministas.
- Expresiones regulares y lema del bombeo.
- Gramáticas libres de contexto y autómatas de pila.
- Máquinas de Turing y tesis de Church-Turing.
- Decidibilidad e indecidibilidad.
- Reducibilidad de problemas.
- Clases de complejidad P, NP, NP-completo, PSPACE, L y NL.
- Análisis de algoritmos y complejidad computacional.

También se documentan los casos de prueba y los resultados obtenidos durante la verificación del sistema.

## Despliegue web

La aplicación puede desplegarse utilizando Streamlit Community Cloud.

Pasos generales:

1. Acceder a [Streamlit Community Cloud](https://share.streamlit.io/).
2. Iniciar sesión con GitHub.
3. Seleccionar el repositorio `GraphLab-TC-UNAH`.
4. Seleccionar la rama que contiene la versión integrada del proyecto.
5. Indicar `streamlit_app.py` como archivo principal.
6. Configurar las dependencias si es necesario.
7. Iniciar el despliegue.

## Objetivo académico

GraphLab TC busca facilitar el aprendizaje práctico de los conceptos relacionados con grafos, alcanzabilidad y problemas de decisión.

Mediante la implementación y visualización de algoritmos, permite relacionar los fundamentos matemáticos de la Teoría de la Computación con su aplicación en el desarrollo de software.