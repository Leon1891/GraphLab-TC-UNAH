
# GraphLab TC - Informe de algoritmos

## 1. Búsqueda en anchura (BFS)

BFS (Breadth-First Search) es un algoritmo de recorrido
de grafos que explora los vértices por niveles.

Utiliza una cola FIFO para procesar primero los vértices
que fueron descubiertos antes.

### Funcionamiento
1. Introduce el vértice de origen en la cola.
2. Extrae el primer vértice.
3. Examina sus vecinos en orden alfabético.
4. Agrega los vecinos que todavía no fueron descubiertos.
5. Repite hasta encontrar el destino o vaciar la cola.
6. Reconstruye la ruta mediante el registro de padres.

### Complejidad
- Tiempo: O(V + E).
- Espacio: O(V).

### Propiedad
BFS encuentra una ruta con el menor número de aristas
en un grafo no ponderado.

## 2. Búsqueda en profundidad (DFS)

DFS (Depth-First Search) explora un camino hasta donde
sea posible antes de retroceder.

Utiliza una pila para administrar los vértices pendientes.

### Funcionamiento
1. Introduce el origen en la pila.
2. Extrae el último vértice agregado.
3. Examina sus vecinos en orden alfabético.
4. Agrega los vecinos no descubiertos.
5. Continúa hasta encontrar el destino o vaciar la pila.
6. Reconstruye la ruta mediante el registro de padres.

### Complejidad
- Tiempo: O(V + E).
- Espacio: O(V).

### Propiedad
DFS permite determinar alcanzabilidad y encontrar una ruta,
pero no garantiza que sea la más corta.

## 3. Problema de cobertura de vértices

Vertex Cover consiste en encontrar un conjunto de
vértices que cubra todas las aristas del grafo.

Para este proyecto se ignora la orientación de las
aristas y se eliminan duplicados.

### Verificación
Una selección es válida si cada arista tiene al menos
uno de sus extremos dentro del conjunto seleccionado.

### Resolución
Se utiliza búsqueda exhaustiva mediante combinaciones
de vértices, comenzando por las de menor tamaño.

Se busca una cobertura con tamaño máximo K.

### Complejidad
La búsqueda exhaustiva puede requerir explorar hasta
2^V subconjuntos.

Su costo es exponencial, por lo que se limita a grafos
de un máximo de 16 vértices.

La verificación de una selección puede realizarse
en O(V + E), considerando la construcción de la
representación del grafo.

## 4. Comparación

| Característica | BFS | DFS |
|---|---|---|
| Estructura | Cola | Pila |
| Exploración | Por niveles | Por profundidad |
| Ruta mínima | Sí | No garantizada |
| Tiempo | O(V+E) | O(V+E) |
| Espacio | O(V) | O(V) |

## 5. Contrato de integración

BFS y DFS devuelven:

- alcanzable
- ruta
- visitados
- pasos

Vertex Cover devuelve:

- existe
- cobertura

Los algoritmos no modifican el grafo recibido
como parámetro.

## 6. Limitaciones

La búsqueda exacta de Vertex Cover está limitada
a 16 vértices para evitar tiempos de ejecución
excesivos en instancias grandes.
