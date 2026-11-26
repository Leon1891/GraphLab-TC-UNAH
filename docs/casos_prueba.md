# Casos de prueba – GraphLab TC

## 1. Introducción

Este documento presenta los casos de prueba definidos para verificar el funcionamiento de GraphLab TC, una aplicación educativa desarrollada para explorar grafos dirigidos, analizar problemas de alcanzabilidad y resolver instancias pequeñas del problema de decisión Vertex Cover.

Las pruebas permiten comprobar que las operaciones principales del sistema producen resultados correctos, que los algoritmos respetan las condiciones establecidas y que las entradas inválidas son controladas adecuadamente.

Se consideran pruebas de los siguientes componentes:

- Administración y validación de grafos.
- Búsqueda en anchura (BFS).
- Búsqueda en profundidad (DFS).
- Problema de decisión Vertex Cover.
- Verificación de soluciones.
- Integración de los componentes con la interfaz.

## 2. Entorno de pruebas

| Elemento | Descripción |
|---|---|
| Proyecto | GraphLab TC |
| Lenguaje | Python |
| Interfaz | Streamlit |
| Framework de pruebas | pytest |
| Visualización | NetworkX y Plotly |
| Sistema de pruebas | Entorno virtual de Python |
| Comando de ejecución | `python -m pytest -q` |
| Fecha de ejecución | 25 de noviembre de 2026 |

## 3. Criterios de aceptación

Se considera que una prueba cumple satisfactoriamente cuando:

1. El sistema produce el resultado esperado para una entrada válida.
2. Los algoritmos identifican correctamente la existencia o inexistencia de rutas.
3. Las rutas encontradas respetan la dirección de las aristas.
4. BFS encuentra una ruta con la menor cantidad de aristas en grafos no ponderados.
5. DFS encuentra una ruta válida cuando existe.
6. Vertex Cover identifica correctamente si existe una cobertura dentro del límite K.
7. Las soluciones de Vertex Cover cubren todas las aristas.
8. Las entradas inválidas producen errores controlados.
9. Los algoritmos no modifican la estructura original del grafo.
10. La interfaz evita mostrar resultados correspondientes a configuraciones o grafos anteriores.

## 4. Casos de prueba

### 4.1. Pruebas de administración de grafos

**CP-01. Creación de un vértice**

- Objetivo: comprobar que el sistema permite agregar un vértice válido.
- Entrada: grafo vacío y nombre de vértice "A".
- Resultado esperado: el vértice A se agrega correctamente.
- Criterio de aceptación: A aparece en la lista de vértices.

**CP-02. Registro de una arista válida**

- Objetivo: verificar la creación de una conexión dirigida.
- Entrada: vértices A y B; arista A → B.
- Resultado esperado: la arista se incorpora al grafo.
- Criterio de aceptación: la lista de aristas contiene [A, B].

**CP-03. Rechazo de un vértice duplicado**

- Objetivo: comprobar la validación de nombres repetidos.
- Entrada: crear el vértice A dos veces.
- Resultado esperado: el sistema rechaza la segunda operación.
- Criterio de aceptación: se genera un error controlado y no se duplica el vértice.

**CP-04. Rechazo de una arista con vértices inexistentes**

- Objetivo: verificar que no se registren conexiones hacia vértices que no existen.
- Entrada: grafo con vértice A e intento de crear A → B sin haber creado B.
- Resultado esperado: el sistema rechaza la operación.
- Criterio de aceptación: la estructura del grafo permanece sin esa arista.

### 4.2. Pruebas del algoritmo BFS

Para los siguientes casos se utiliza el grafo dirigido:

V = {A, B, C, D, E}

E = {(A, B), (A, D), (B, C), (C, E), (D, E)}

**CP-05. Búsqueda de una ruta existente mediante BFS**

- Objetivo: comprobar que BFS identifica una ruta entre dos vértices conectados.
- Entrada: origen A y destino E.
- Resultado esperado: alcanzable = verdadero.
- Ruta esperada: A → D → E o A → B → C → E, dependiendo del orden de exploración definido por el algoritmo.
- Criterio de aceptación: la ruta comienza en A, termina en E y cada conexión existe en el grafo.

**CP-06. Búsqueda de una ruta inexistente mediante BFS**

- Objetivo: verificar que BFS identifique destinos no alcanzables.
- Entrada: grafo con vértices A y B, sin aristas; origen A y destino B.
- Resultado esperado: alcanzable = falso.
- Ruta esperada: lista vacía.
- Criterio de aceptación: el algoritmo informa que no existe una ruta.

**CP-07. Búsqueda con origen y destino iguales**

- Objetivo: comprobar el comportamiento cuando ambos parámetros representan el mismo vértice.
- Entrada: origen A y destino A.
- Resultado esperado: alcanzable = verdadero.
- Ruta esperada: [A].
- Criterio de aceptación: el algoritmo reconoce que no se necesita recorrer ninguna arista para llegar al mismo vértice.

### 4.3. Pruebas del algoritmo DFS

**CP-08. Búsqueda de una ruta existente mediante DFS**

- Objetivo: verificar que DFS encuentre una ruta válida.
- Entrada: grafo dirigido del apartado 4.2; origen A y destino E.
- Resultado esperado: alcanzable = verdadero.
- Ruta esperada: una secuencia válida desde A hasta E.
- Criterio de aceptación: todos los pares consecutivos de la ruta corresponden a aristas existentes y respetan su dirección.

**CP-09. Exploración de un grafo con ciclos**

- Objetivo: comprobar que DFS controle los vértices visitados y no entre en un ciclo infinito.
- Entrada: grafo con aristas A → B, B → C y C → A; origen A y destino C.
- Resultado esperado: alcanzable = verdadero.
- Ruta esperada: A → B → C.
- Criterio de aceptación: el algoritmo termina correctamente y no repite vértices procesados en la lista de visitados.

### 4.4. Pruebas del problema Vertex Cover

Para estos casos se considera la interpretación no dirigida de las aristas.

**CP-10. Existencia de una cobertura válida**

- Objetivo: verificar que el algoritmo encuentre una cobertura dentro del límite K.
- Entrada: grafo con V = {A, B, C} y E = {{A, B}, {B, C}}; K = 1.
- Resultado esperado: existe = verdadero.
- Cobertura esperada: {B}.
- Criterio de aceptación: el vértice B cubre las dos aristas.

**CP-11. Inexistencia de cobertura dentro del límite K**

- Objetivo: comprobar que el sistema identifique cuando no existe una solución que respete el límite.
- Entrada: grafo con V = {A, B, C} y E = {{A, B}, {B, C}, {A, C}}; K = 1.
- Resultado esperado: existe = falso.
- Criterio de aceptación: ninguna selección de un solo vértice cubre las tres aristas.

**CP-12. Verificación de una cobertura incorrecta**

- Objetivo: comprobar que la función de verificación rechace una selección que no cubra todas las aristas.
- Entrada: grafo con V = {A, B, C} y E = {{A, B}, {B, C}}; selección {A}; K = 1.
- Resultado esperado: verificación = falso.
- Criterio de aceptación: la arista B — C no queda cubierta.

**CP-13. Verificación de una cobertura válida**

- Objetivo: comprobar que la función de verificación acepte una selección correcta.
- Entrada: grafo con V = {A, B, C} y E = {{A, B}, {B, C}}; selección {B}; K = 1.
- Resultado esperado: verificación = verdadero.
- Criterio de aceptación: todas las aristas tienen al menos un extremo perteneciente a la selección.

## 5. Pruebas de integración de la interfaz

Además de las pruebas automatizadas de los algoritmos, se establecen las siguientes comprobaciones funcionales de la aplicación Streamlit.

| Código | Comprobación | Resultado esperado |
|---|---|---|
| PI-01 | Ejecutar BFS desde la interfaz | Mostrar alcanzabilidad, ruta y recorrido |
| PI-02 | Ejecutar DFS desde la interfaz | Mostrar alcanzabilidad y recorrido |
| PI-03 | Modificar el grafo después de una búsqueda | Solicitar una nueva ejecución |
| PI-04 | Cambiar origen o destino | Solicitar ejecutar nuevamente el algoritmo |
| PI-05 | Ejecutar Vertex Cover con cinco vértices | Permitir la búsqueda exacta |
| PI-06 | Ejecutar Vertex Cover con más de 16 vértices | Bloquear la ejecución y mostrar advertencia |
| PI-07 | Cambiar el grafo después de obtener una cobertura | Evitar mostrar la solución anterior como vigente |
| PI-08 | Exportar el grafo | Descargar un archivo JSON |

**Nota:** estas comprobaciones de interfaz deben registrarse como realizadas únicamente después de ejecutarlas manualmente en Streamlit. No forman parte necesariamente de las 48 pruebas automatizadas.

## 6. Resultados generales de la ejecución automatizada

El proyecto cuenta con una suite de pruebas automatizadas ejecutada mediante pytest.

Comando utilizado:

```bash
python -m pytest -q
```

Resultado obtenido en la ejecución del 25 de noviembre de 2026:

```text
................................................                         [100%]
48 passed in 0.17s
```

Resumen:

| Indicador | Resultado |
|---|---:|
| Pruebas automatizadas aprobadas | 48 |
| Pruebas automatizadas fallidas | 0 |
| Tiempo de ejecución | 0.17 segundos |
| Estado general | Aprobado |

La ejecución confirma que las 48 pruebas automatizadas existentes finalizaron satisfactoriamente en el momento de la ejecución.

Los casos CP-01 a CP-13 representan los escenarios funcionales documentados del sistema. La salida global de pytest no identifica por sí sola qué prueba individual corresponde a cada escenario; por ello, no se atribuye a cada caso un resultado automatizado individual sin revisar su implementación específica.

## 7. Conclusiones

Las pruebas permiten establecer criterios para verificar la funcionalidad de GraphLab TC y comprobar el comportamiento esperado de sus principales componentes.

Los algoritmos BFS y DFS permiten analizar la alcanzabilidad en grafos dirigidos, mientras que Vertex Cover permite estudiar un problema de decisión de mayor complejidad computacional.

Las validaciones de entrada ayudan a mantener la integridad de los grafos, y las pruebas de integración permiten comprobar que la interfaz presente resultados correspondientes a la configuración actual.

La ejecución automatizada reportó 48 pruebas aprobadas y ninguna fallida, lo que constituye evidencia favorable del funcionamiento del código en el momento de la prueba.

Se recomienda conservar la ejecución de la suite automatizada después de cada modificación importante del proyecto y complementar estos resultados con comprobaciones manuales de la interfaz.