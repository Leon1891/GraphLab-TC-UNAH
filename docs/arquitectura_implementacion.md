# Arquitectura e implementación de GraphLab TC-UNAH

## 1. Introducción

GraphLab TC-UNAH es una aplicación desarrollada como apoyo al estudio de la Teoría de la Computación. Su propósito principal es permitir la creación, exploración y análisis de grafos dirigidos, así como resolver problemas relacionados con la alcanzabilidad y los problemas de decisión.

La aplicación permite construir grafos, visualizar sus conexiones, ejecutar los algoritmos de búsqueda en anchura (BFS) y búsqueda en profundidad (DFS), comparar sus resultados y resolver instancias pequeñas del problema Vertex Cover.

El sistema fue desarrollado utilizando Python y Streamlit, con una arquitectura modular que separa la lógica de los grafos, los algoritmos, la interfaz gráfica, las herramientas de visualización y las pruebas.

## 2. Arquitectura general del sistema

El proyecto utiliza una arquitectura modular. Cada directorio contiene componentes con responsabilidades específicas, lo que facilita el mantenimiento, la comprensión y la ampliación del sistema.

La arquitectura se divide en los siguientes módulos:

- **Core:** contiene las operaciones fundamentales para crear y administrar grafos.
- **Algoritmos:** implementa los procedimientos de búsqueda y resolución de problemas.
- **Interfaz:** presenta las herramientas con las que interactúa el usuario.
- **Utilidades:** contiene funciones auxiliares para representar gráficamente los resultados.
- **Tests:** reúne las pruebas automatizadas utilizadas para comprobar el funcionamiento del sistema.
- **Ejemplos:** contiene grafos de referencia que pueden utilizarse para realizar pruebas y demostraciones.
- **Docs:** almacena la documentación técnica y teórica del proyecto.

## 3. Estructura del proyecto

La organización principal de GraphLab TC-UNAH es la siguiente:

```text
GraphLab-TC-UNAH/
│
├── algoritmos/
│   ├── __init__.py
│   ├── bfs.py
│   ├── dfs.py
│   └── vertex_cover.py
│
├── core/
│   ├── __init__.py
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
│   ├── __init__.py
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
│   ├── __init__.py
│   └── visualizacion.py
│
└── streamlit_app.py
```

### 3.1. Archivo principal: streamlit_app.py

Es el punto de entrada de la aplicación. Se encarga de configurar la página de Streamlit, establecer el título, el icono y la distribución, y organizar la navegación entre las diferentes secciones.

Desde este archivo se integran los módulos de:

- Editor de grafos.
- Exploración BFS y DFS.
- Comparación de algoritmos.
- Resolución de Vertex Cover.
- Información del proyecto.

### 3.2. Módulo core

El archivo `core/grafo.py` contiene las operaciones principales para administrar la estructura de los grafos.

Entre sus responsabilidades se encuentran:

- Crear un grafo vacío.
- Agregar vértices.
- Agregar aristas.
- Eliminar vértices.
- Eliminar aristas.
- Validar los nombres de los vértices.
- Comprobar que las aristas conecten vértices existentes.
- Importar y exportar grafos en formato JSON.

Este módulo centraliza las validaciones para evitar que los demás componentes tengan que repetir las mismas comprobaciones.

### 3.3. Módulo algoritmos

El directorio `algoritmos/` contiene la implementación de los procedimientos principales del proyecto.

**a) BFS (Breadth-First Search)**

El algoritmo de búsqueda en anchura explora el grafo por niveles, comenzando desde un vértice de origen. Utiliza una cola para controlar el orden de exploración.

Su función dentro de la aplicación es determinar si un vértice destino es alcanzable desde un origen y recuperar una ruta cuando existe.

**b) DFS (Depth-First Search)**

El algoritmo de búsqueda en profundidad explora una rama del grafo hasta donde sea posible antes de regresar y continuar con otras alternativas.

Se utiliza para estudiar la conectividad desde un vértice de origen y obtener una ruta cuando el destino puede alcanzarse.

**c) Vertex Cover**

El módulo `vertex_cover.py` implementa una búsqueda exacta para resolver instancias pequeñas del problema Vertex Cover.

El problema consiste en encontrar un conjunto de vértices que cubra todas las aristas de un grafo no dirigido. Una arista está cubierta cuando al menos uno de sus extremos pertenece al conjunto seleccionado.

La implementación permite buscar una cobertura de tamaño máximo `k` y verificar si una selección propuesta cubre correctamente todas las aristas.

Para este problema, las aristas del grafo se interpretan como no dirigidas. Por ello, una conexión entre A y B se considera cubierta tanto si se selecciona A como si se selecciona B.

La búsqueda exacta está limitada a grafos de hasta 16 vértices. Este límite es una decisión de implementación para mantener el tiempo de ejecución controlado; no representa un límite teórico del problema.

### 3.4. Módulo interfaz

El directorio `interfaz/` contiene los componentes visuales que permiten utilizar las funcionalidades del sistema.

- `editor.py`: permite construir y modificar grafos mediante la interfaz.
- `explorador.py`: permite ejecutar BFS, DFS y resolver el problema Vertex Cover, mostrando los resultados correspondientes.
- `comparacion.py`: presenta una comparación entre los algoritmos de exploración, considerando sus resultados y complejidad.

La interfaz se construye con Streamlit, lo que permite interactuar con los grafos sin necesidad de utilizar directamente la consola de Python.

### 3.5. Módulo utilidades

El archivo `utilidades/visualizacion.py` contiene funciones auxiliares para representar los grafos.

Se utiliza NetworkX para trabajar con la estructura gráfica y Plotly para generar representaciones visuales interactivas.

La visualización facilita la comprensión de los vértices, las conexiones y los recorridos realizados por los algoritmos.

### 3.6. Módulo tests

El directorio `tests/` contiene las pruebas automatizadas del proyecto.

Se organiza en archivos separados para comprobar diferentes componentes:

- `test_grafo.py`: operaciones y validaciones de los grafos.
- `test_bfs.py`: funcionamiento de la búsqueda en anchura.
- `test_dfs.py`: funcionamiento de la búsqueda en profundidad.
- `test_vertex_cover.py`: resolución y verificación de Vertex Cover.

Las pruebas permiten detectar errores y comprobar que los componentes principales respondan de acuerdo con los resultados esperados.

## 4. Representación interna de los grafos

GraphLab TC utiliza una representación mediante listas de vértices y aristas.

Un grafo se representa como un diccionario de Python con dos propiedades principales:

- `vertices`: contiene la lista de vértices.
- `aristas`: contiene las conexiones entre los vértices.

Ejemplo:

```python
grafo = {
    "vertices": ["A", "B", "C", "D"],
    "aristas": [
        ["A", "B"],
        ["A", "C"],
        ["B", "D"],
        ["C", "D"]
    ]
}
```

En este ejemplo, los vértices son A, B, C y D. Las aristas representan conexiones dirigidas: por ejemplo, A → B indica que existe una conexión desde A hacia B.

Esta representación permite almacenar, modificar y procesar los grafos mediante las funciones del módulo `core`.

## 5. Flujo de funcionamiento del sistema

El funcionamiento general de la aplicación sigue el siguiente proceso:

1. El usuario ingresa a GraphLab TC desde la interfaz principal.
2. Selecciona el editor de grafos para crear un grafo o modificar uno existente.
3. El módulo `core` valida las operaciones realizadas, como agregar vértices y aristas.
4. El grafo actualizado queda disponible para las demás secciones de la aplicación.
5. El usuario selecciona una herramienta de exploración o análisis.
6. La interfaz solicita los datos necesarios, como el vértice de origen, el destino o el valor de `k`.
7. Se ejecuta el algoritmo correspondiente.
8. El resultado se presenta mediante información textual, métricas y representaciones gráficas cuando corresponde.
9. El usuario puede continuar explorando el grafo o exportarlo en formato JSON.

Este flujo mantiene separadas las operaciones internas del grafo, el procesamiento algorítmico y la presentación de resultados.

## 6. Contrato de funcionamiento de los algoritmos

Los algoritmos BFS y DFS reciben como entrada un grafo, un vértice de origen y un vértice de destino.

Las funciones principales son:

```python
bfs(grafo, origen, destino)
dfs(grafo, origen, destino)
```

Ambas devuelven un diccionario con información sobre la exploración:

```python
{
    "alcanzable": True,
    "ruta": ["A", "B", "D"],
    "visitados": ["A", "B", "C", "D"],
    "pasos": []
}
```

Los campos representan:

- `alcanzable`: indica si existe una ruta desde el origen hasta el destino.
- `ruta`: contiene los vértices de una ruta encontrada.
- `visitados`: registra los vértices explorados.
- `pasos`: contiene información del procedimiento de exploración.

Si no existe una ruta, el campo `alcanzable` indica `False` y la ruta se devuelve vacía. Si el origen y el destino son iguales, la ruta contiene únicamente ese vértice.

Los algoritmos trabajan sobre la información del grafo sin modificar la estructura original recibida como entrada.

## 7. Análisis de complejidad

La complejidad permite estudiar el consumo de recursos de un algoritmo conforme aumenta el tamaño de la entrada.

Para los algoritmos de exploración se consideran:

- V: cantidad de vértices.
- E: cantidad de aristas.

### 7.1. Complejidad de BFS

BFS visita los vértices alcanzables y examina las aristas correspondientes mediante una estructura de cola.

- **Tiempo:** O(V + E).
- **Espacio auxiliar:** O(V).

Su principal ventaja es que encuentra una ruta con el menor número de aristas cuando el grafo no tiene pesos.

### 7.2. Complejidad de DFS

DFS explora los vértices utilizando una estrategia de profundidad.

- **Tiempo:** O(V + E).
- **Espacio auxiliar:** O(V).

Puede utilizarse para explorar la estructura del grafo y encontrar una ruta, pero no garantiza que la ruta encontrada tenga la menor cantidad de aristas.

### 7.3. Complejidad de Vertex Cover

Vertex Cover es un problema de optimización combinatoria. Su versión de decisión pregunta si existe una cobertura de vértices cuyo tamaño sea como máximo `k`.

Para un grafo no dirigido, la versión de decisión de Vertex Cover es NP-completa.

La implementación de GraphLab TC utiliza una búsqueda exacta sobre subconjuntos de vértices. En el peor caso, el número de subconjuntos considerados crece exponencialmente con la cantidad de vértices.

Una cota general para una búsqueda exhaustiva que verifica cada subconjunto recorriendo las aristas es O(2^V · (V + E)). El costo exacto puede variar según las optimizaciones y la estrategia utilizada en la implementación.

Por esta razón, el sistema establece un límite de 16 vértices para ejecutar la búsqueda exacta.

## 8. Tecnologías utilizadas

Las tecnologías principales del proyecto son:

| Tecnología | Utilización |
|---|---|
| Python | Lenguaje de programación principal. |
| Streamlit | Desarrollo de la interfaz interactiva. |
| NetworkX | Apoyo para la representación y manipulación de grafos. |
| Plotly | Generación de visualizaciones interactivas. |
| Pytest | Ejecución de pruebas automatizadas. |
| JSON | Formato para importar y exportar grafos. |
| Git y GitHub | Control de versiones y colaboración en el desarrollo. |

## 9. Ejecución del proyecto

Para ejecutar GraphLab TC-UNAH se necesita tener Python instalado y acceder a la carpeta raíz del proyecto.

En Windows PowerShell, los pasos generales son los siguientes:

**Paso 1. Activar el entorno virtual**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Paso 2. Instalar las dependencias**

Si el proyecto incluye un archivo `requirements.txt`, ejecutar:

```powershell
pip install -r requirements.txt
```

**Paso 3. Iniciar la aplicación**

```powershell
streamlit run streamlit_app.py
```

Streamlit abrirá la aplicación en el navegador.

**Paso 4. Ejecutar las pruebas automatizadas**

Para comprobar el funcionamiento de los módulos se utiliza:

```powershell
python -m pytest -q
```

## 10. Resultados de las pruebas

Durante la verificación del proyecto se ejecutó la suite de pruebas automatizadas mediante Pytest.

El resultado obtenido el 25 de noviembre de 2026 fue:

```text
................................................ [100%]
48 passed in 0.17s
```

Esto indica que se aprobaron 48 pruebas automatizadas, sin fallos en esa ejecución.

Este resultado constituye una comprobación del funcionamiento de los componentes cubiertos por la suite de pruebas. Las verificaciones manuales de la interfaz deben documentarse por separado, de acuerdo con las pruebas que efectivamente se hayan realizado.

## 11. Consideraciones y limitaciones

GraphLab TC fue diseñado como una herramienta educativa para experimentar con grafos y comprender el comportamiento de los algoritmos.

Entre sus principales consideraciones se encuentran:

- Los grafos utilizados por BFS y DFS son dirigidos y no ponderados.
- BFS encuentra rutas mínimas en cantidad de aristas, no en distancia o peso.
- DFS encuentra rutas posibles, pero no garantiza una ruta mínima.
- Vertex Cover interpreta las conexiones como aristas no dirigidas.
- La búsqueda exacta de Vertex Cover se limita a 16 vértices para controlar el crecimiento del tiempo de ejecución.
- La aplicación no pretende sustituir herramientas especializadas para analizar grafos de gran tamaño.

Estas decisiones permiten mantener una aplicación funcional y adecuada para fines académicos.

## 12. Conclusión

La arquitectura modular de GraphLab TC-UNAH permite integrar las operaciones fundamentales de los grafos, los algoritmos de exploración, la resolución de un problema de decisión y la representación visual de los resultados.

La separación entre lógica, algoritmos e interfaz facilita el mantenimiento del código y permite ampliar el proyecto en el futuro.

La implementación de BFS y DFS permite estudiar la alcanzabilidad en grafos dirigidos, mientras que Vertex Cover introduce un problema de mayor complejidad computacional y permite relacionar la práctica con los conceptos de la clase de complejidad NP.

Finalmente, las 48 pruebas automatizadas aprobadas constituyen evidencia de verificación del código cubierto por la suite, complementando la documentación teórica y técnica del proyecto.