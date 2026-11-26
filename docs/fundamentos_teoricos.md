# Fundamentos teóricos de Teoría de la Computación

## Proyecto GraphLab TC – UNAH

## 1. Introducción

La Teoría de la Computación es una rama de las ciencias de la computación que estudia los modelos matemáticos utilizados para representar procesos computacionales, los problemas que pueden resolverse mediante algoritmos y los recursos necesarios para hacerlo.

Esta área permite comprender qué significa computar, cuáles son los límites de los algoritmos y cómo se pueden clasificar los problemas según su dificultad.

El proyecto GraphLab TC aplica estos fundamentos mediante la creación y exploración de grafos dirigidos, el análisis de alcanzabilidad utilizando los algoritmos Breadth-First Search (BFS) y Depth-First Search (DFS), y la resolución de un problema de decisión conocido como Vertex Cover.

Este documento presenta los conceptos fundamentales que respaldan el desarrollo del proyecto.

## 2. Fundamentos matemáticos

### 2.1. Conjuntos

Un conjunto es una colección bien definida de elementos distintos.

Se representa mediante llaves. Por ejemplo:

A = {1, 2, 3, 4}

En teoría de conjuntos se utilizan operaciones como:

- Unión: reúne los elementos de dos conjuntos.
- Intersección: obtiene los elementos comunes.
- Diferencia: obtiene los elementos que pertenecen a un conjunto, pero no al otro.
- Subconjunto: indica que todos los elementos de un conjunto pertenecen a otro.

**Aplicación en GraphLab TC:**

Un grafo se construye utilizando un conjunto de vértices y un conjunto de aristas. Por ejemplo, los vértices pueden representarse mediante:

V = {A, B, C, D}

### 2.2. Alfabetos

Un alfabeto es un conjunto finito y no vacío de símbolos. Generalmente se representa con la letra griega Σ.

Ejemplo:

Σ = {0, 1}

Este alfabeto contiene dos símbolos: cero y uno.

Los alfabetos permiten construir cadenas y definir lenguajes formales.

### 2.3. Cadenas

Una cadena es una secuencia finita de símbolos pertenecientes a un alfabeto.

Si Σ = {0, 1}, algunos ejemplos de cadenas son:

- 0
- 1
- 01
- 101
- 1100

La cadena vacía se representa mediante ε y tiene longitud cero.

La longitud de una cadena se representa como |w|.

Por ejemplo:

Si w = 1011, entonces |w| = 4.

### 2.4. Lenguajes formales

Un lenguaje formal es cualquier conjunto de cadenas construidas a partir de un alfabeto.

Formalmente, si Σ es un alfabeto, un lenguaje L cumple:

L ⊆ Σ*

Donde Σ* representa el conjunto de todas las cadenas finitas que pueden construirse con los símbolos de Σ, incluida la cadena vacía.

Ejemplo:

Sea Σ = {0, 1} y:

L = {0, 00, 000, 0000, ...}

Este lenguaje contiene las cadenas formadas únicamente por uno o más ceros.

Los lenguajes formales son importantes porque permiten describir qué cadenas acepta o reconoce un modelo computacional.

### 2.5. Relaciones y funciones

Una relación entre dos conjuntos A y B es un conjunto de pares ordenados pertenecientes al producto cartesiano A × B.

Una función es un tipo especial de relación que asigna a cada elemento del dominio exactamente un elemento del codominio.

En los grafos dirigidos, las aristas representan relaciones entre vértices.

Por ejemplo:

E = {(A, B), (B, C)}

Indica que existe una conexión dirigida desde A hasta B y otra desde B hasta C.

**Aplicación en GraphLab TC:**

El proyecto utiliza una representación de grafos mediante dos listas:

- `vertices`: almacena los vértices.
- `aristas`: almacena los pares ordenados que representan las conexiones dirigidas.

## 3. Autómatas finitos

Los autómatas finitos son modelos matemáticos utilizados para reconocer lenguajes regulares. Se caracterizan por tener una cantidad finita de estados y procesar una entrada símbolo por símbolo.

### 3.1. Autómata finito determinista (AFD)

Un autómata finito determinista es una máquina que, para cada estado y símbolo de entrada, tiene exactamente una transición definida.

Formalmente, un AFD se representa mediante la quíntupla:

M = (Q, Σ, δ, q₀, F)

Donde:

- Q: conjunto finito de estados.
- Σ: alfabeto de entrada.
- δ: función de transición.
- q₀: estado inicial.
- F: conjunto de estados finales o de aceptación.

La función de transición se define como:

δ: Q × Σ → Q

Esto significa que, al encontrarse en un estado y recibir un símbolo, el autómata pasa a un único estado siguiente.

**Ejemplo:**

Se desea construir un AFD que acepte cadenas binarias que terminen en 1.

Se utilizan dos estados:

- q₀: la cadena leída no termina en 1.
- q₁: la cadena leída termina en 1.

El estado inicial es q₀ y el estado de aceptación es q₁.

| Estado | Entrada 0 | Entrada 1 |
|---|---|---|
| q₀ | q₀ | q₁ |
| q₁ | q₀ | q₁ |

La cadena 101 es aceptada porque termina en 1. La cadena 100 es rechazada porque termina en 0.

### 3.2. Autómata finito no determinista (AFN)

Un autómata finito no determinista es un modelo en el que un estado puede tener varias transiciones posibles para un mismo símbolo de entrada, o incluso ninguna.

Formalmente, su función de transición puede expresarse como:

δ: Q × Σ → P(Q)

Donde P(Q) representa el conjunto potencia de Q.

A diferencia del AFD, un AFN puede explorar diferentes posibilidades de transición. Una cadena es aceptada si existe al menos un recorrido que termina en un estado de aceptación.

También existen AFN con transiciones ε, que permiten cambiar de estado sin consumir un símbolo de entrada.

### 3.3. Expresiones regulares

Una expresión regular es una notación utilizada para describir patrones de cadenas pertenecientes a lenguajes regulares.

Entre sus operadores principales se encuentran:

- Unión: representa una alternativa.
- Concatenación: une dos expresiones.
- Cerradura de Kleene (*): permite repetir una expresión cero o más veces.

Ejemplo:

La expresión regular:

(0|1)*1

Describe las cadenas binarias que terminan en 1.

Las expresiones regulares y los autómatas finitos tienen el mismo poder expresivo: ambos permiten representar exactamente los lenguajes regulares.

### 3.4. Limitaciones de los autómatas finitos

Los autómatas finitos tienen memoria limitada, porque solamente pueden almacenar información mediante una cantidad finita de estados.

Por esta razón, no pueden reconocer todos los lenguajes posibles.

Por ejemplo, el lenguaje:

L = {0ⁿ1ⁿ | n ≥ 0}

Contiene cadenas con la misma cantidad de ceros seguidos de unos.

Un autómata finito no puede reconocer este lenguaje porque necesitaría recordar una cantidad arbitraria de ceros para compararla con la cantidad posterior de unos.

### 3.5. Lema del bombeo para lenguajes regulares

El lema del bombeo es una propiedad utilizada para demostrar que determinados lenguajes no son regulares.

Establece que, si un lenguaje L es regular, existe un número p, llamado longitud de bombeo, tal que toda cadena w perteneciente a L con longitud al menos p puede dividirse en tres partes:

w = xyz

Cumpliendo las siguientes condiciones:

1. |xy| ≤ p.
2. |y| > 0.
3. Para todo i ≥ 0, la cadena xyⁱz pertenece a L.

La tercera condición significa que la parte y puede repetirse cualquier cantidad de veces, incluso cero, sin que la cadena deje de pertenecer al lenguaje.

**Ejemplo de aplicación:**

Para demostrar que L = {0ⁿ1ⁿ | n ≥ 0} no es regular, se supone que es regular y se toma una cadena:

w = 0ᵖ1ᵖ

Debido a la condición |xy| ≤ p, las partes x e y están formadas únicamente por ceros. Además, |y| > 0.

Al eliminar y, es decir, utilizar i = 0, se obtiene una cadena con menos ceros que unos.

Esta cadena ya no pertenece a L, lo que contradice el lema del bombeo.

Por lo tanto, el lenguaje no es regular.

## 4. Gramáticas libres de contexto y autómatas de pila

### 4.1. Gramáticas libres de contexto (GLC)

Una gramática libre de contexto es un sistema formal utilizado para generar lenguajes libres de contexto.

Se representa mediante una cuádrupla:

G = (V, Σ, P, S)

Donde:

- V: conjunto de variables o símbolos no terminales.
- Σ: conjunto de símbolos terminales.
- P: conjunto de producciones.
- S: símbolo inicial.

Las producciones tienen la forma:

A → α

Donde A es un símbolo no terminal y α es una cadena de terminales y no terminales.

**Ejemplo:**

Para generar cadenas de la forma 0ⁿ1ⁿ:

S → 0S1 | ε

Esta gramática permite generar:

- ε
- 01
- 0011
- 000111
- 00001111

La gramática genera cadenas con la misma cantidad de ceros y unos, manteniendo todos los ceros antes de los unos.

### 4.2. Autómatas de pila

Un autómata de pila es un modelo computacional similar a un autómata finito, pero incorpora una estructura adicional llamada pila.

La pila funciona bajo el principio LIFO: el último elemento que entra es el primero que sale.

Esta memoria adicional permite reconocer lenguajes que no pueden ser reconocidos por autómatas finitos.

Por ejemplo, un autómata de pila puede reconocer el lenguaje:

L = {0ⁿ1ⁿ | n ≥ 0}

Puede almacenar información al leer los ceros y utilizarla para comprobar la cantidad de unos posteriores.

Las gramáticas libres de contexto y los autómatas de pila están estrechamente relacionados: los lenguajes libres de contexto son precisamente los lenguajes que pueden reconocer los autómatas de pila no deterministas.

## 5. Máquinas de Turing

### 5.1. Definición

Una máquina de Turing es un modelo matemático de computación que permite representar procesos algorítmicos mediante una cinta, un cabezal de lectura y escritura y un conjunto de estados.

Una máquina de Turing puede realizar operaciones de lectura, escritura y desplazamiento sobre la cinta.

Formalmente, una máquina de Turing determinista puede representarse mediante:

M = (Q, Σ, Γ, δ, q₀, qₐ, qᵣ)

Donde:

- Q: conjunto finito de estados.
- Σ: alfabeto de entrada.
- Γ: alfabeto de la cinta.
- δ: función de transición.
- q₀: estado inicial.
- qₐ: estado de aceptación.
- qᵣ: estado de rechazo.

La cinta funciona como un espacio de almacenamiento potencialmente ilimitado y el cabezal permite leer y modificar sus símbolos.

### 5.2. Funcionamiento

Una máquina de Turing comienza en un estado inicial y procesa la entrada almacenada en la cinta.

En cada paso:

1. Lee el símbolo ubicado bajo el cabezal.
2. Consulta la función de transición.
3. Cambia de estado.
4. Escribe un símbolo en la cinta, si corresponde.
5. Mueve el cabezal hacia la izquierda o derecha, según la transición.

El proceso continúa hasta alcanzar un estado de aceptación, un estado de rechazo o permanecer ejecutándose indefinidamente.

### 5.3. Variantes de las máquinas de Turing

Existen diferentes variantes de máquinas de Turing, entre ellas:

- Máquina de Turing no determinista: puede tener varias transiciones posibles para una misma configuración.
- Máquina de Turing multicinta: utiliza varias cintas y cabezales.
- Máquina de Turing con cinta bidireccional: permite desplazarse en ambas direcciones.
- Máquina de Turing universal: puede simular el comportamiento de otras máquinas de Turing a partir de su descripción y entrada.

Estas variantes pueden facilitar la descripción de algoritmos, pero las variantes estándar equivalentes mantienen el mismo poder computacional en términos de qué problemas pueden resolver.

### 5.4. Tesis de Church-Turing

La tesis de Church-Turing establece que cualquier procedimiento que pueda considerarse efectivamente calculable puede ser realizado por una máquina de Turing.

Esta afirmación conecta la noción intuitiva de algoritmo con un modelo matemático formal de computación.

Es importante señalar que se trata de una tesis, no de un teorema matemático demostrable, porque la noción de procedimiento efectivo es una idea informal.

## 6. Decidibilidad e indecidibilidad

### 6.1. Problemas decidibles

Un problema es decidible cuando existe un algoritmo que siempre termina y proporciona una respuesta correcta para cualquier entrada válida.

En los problemas de decisión, las respuestas posibles son:

- Sí.
- No.

**Ejemplo:**

Determinar si existe una ruta entre dos vértices de un grafo finito.

Este problema es decidible porque se puede utilizar un algoritmo de exploración como BFS o DFS, que termina después de visitar una cantidad finita de vértices y aristas.

**Aplicación en GraphLab TC:**

El módulo de alcanzabilidad determina si existe un camino dirigido entre un vértice de origen y uno de destino.

### 6.2. Problemas indecidibles

Un problema es indecidible cuando no existe un algoritmo que pueda proporcionar una respuesta correcta y terminar para todas las posibles entradas del problema.

Un ejemplo clásico es el problema de la parada (Halting Problem).

Este problema consiste en determinar si un programa o máquina de Turing se detendrá o continuará ejecutándose indefinidamente para una entrada determinada.

Alan Turing demostró que no existe un algoritmo general que pueda resolver correctamente todos los casos del problema de la parada.

La indecidibilidad demuestra que existen límites fundamentales sobre lo que puede resolverse mediante algoritmos.

## 7. Reducibilidad

La reducibilidad es una técnica utilizada para relacionar problemas computacionales y demostrar su dificultad.

Un problema A se reduce a un problema B cuando existe una transformación efectiva que convierte las instancias de A en instancias de B, conservando la respuesta.

En una reducción many-one:

A ≤ₘ B

Esto significa que, si se pudiera resolver B eficientemente, también se podría resolver A mediante la transformación correspondiente y la solución de B.

### 7.1. Ejemplo: reducción de Vertex Cover a Independent Set

El problema Independent Set pregunta si un grafo contiene un conjunto de al menos k vértices donde ningún par de vértices está conectado por una arista.

En un grafo no dirigido G = (V, E), un conjunto C es un Vertex Cover si cada arista tiene al menos uno de sus extremos en C.

Un conjunto I es independiente si ninguna arista tiene ambos extremos en I.

Se cumple que:

C es un Vertex Cover si y solo si V − C es un conjunto independiente.

Por lo tanto:

G tiene un Vertex Cover de tamaño máximo k si y solo si G tiene un conjunto independiente de tamaño al menos |V| − k.

Esta relación permite transformar una instancia de Vertex Cover en una instancia de Independent Set y demuestra cómo se relacionan ambos problemas.

## 8. Complejidad computacional

La complejidad computacional estudia los recursos que necesita un algoritmo para resolver un problema.

Los recursos más utilizados para medir la eficiencia son:

- Tiempo: cantidad de operaciones o pasos de ejecución.
- Espacio: cantidad de memoria adicional necesaria.

La complejidad suele expresarse mediante notación asintótica, especialmente la notación O grande.

### 8.1. Notación O grande

La notación O grande describe una cota superior asintótica del crecimiento de un algoritmo.

Por ejemplo:

O(n)

Indica un crecimiento lineal respecto al tamaño de la entrada.

Algunos órdenes de complejidad comunes son:

| Complejidad | Descripción |
|---|---|
| O(1) | Constante |
| O(log n) | Logarítmica |
| O(n) | Lineal |
| O(n log n) | Lineal-logarítmica |
| O(n²) | Cuadrática |
| O(2ⁿ) | Exponencial |
| O(n!) | Factorial |

En general, los algoritmos con crecimiento polinómico suelen ser más manejables que aquellos cuyo tiempo crece exponencialmente o factorialmente.

### 8.2. Clase P

La clase P contiene los problemas de decisión que pueden resolverse en tiempo polinómico mediante una máquina de Turing determinista.

Esto significa que existe un algoritmo cuyo tiempo de ejecución está acotado por una función polinómica del tamaño de la entrada.

Ejemplos de problemas que pueden resolverse en tiempo polinómico incluyen:

- Determinar si existe una ruta entre dos vértices de un grafo.
- Encontrar una ruta de menor cantidad de aristas mediante BFS en un grafo no ponderado.
- Ordenar una lista mediante algoritmos eficientes.

El problema de alcanzabilidad implementado en GraphLab TC pertenece a P.

### 8.3. Clase NP

La clase NP contiene los problemas de decisión cuyas respuestas afirmativas pueden verificarse en tiempo polinómico mediante una máquina de Turing determinista, utilizando un certificado adecuado.

Esto no significa que todos los problemas de NP sean difíciles de resolver. Significa que, cuando se proporciona una solución candidata válida, puede comprobarse eficientemente.

**Ejemplo: Vertex Cover**

Dado un grafo no dirigido G = (V, E) y un entero k, se pregunta:

¿Existe un conjunto de vértices C, con |C| ≤ k, que cubra todas las aristas?

Un certificado es el conjunto de vértices seleccionado.

Para verificarlo se comprueba:

1. Que todos los vértices seleccionados pertenezcan a V.
2. Que el tamaño de C no supere k.
3. Que cada arista tenga al menos uno de sus extremos en C.

Esta verificación puede realizarse en tiempo polinómico respecto al tamaño de la entrada.

Por eso Vertex Cover pertenece a NP.

### 8.4. Relación entre P y NP

Se sabe que:

P ⊆ NP

Esto se debe a que, si un problema puede resolverse en tiempo polinómico, también puede verificarse en tiempo polinómico.

Sin embargo, no se sabe si:

P = NP

Esta es una de las preguntas abiertas más importantes de la informática teórica y las matemáticas.

### 8.5. Problemas NP-completos

Un problema es NP-completo cuando cumple dos condiciones:

1. Pertenece a NP.
2. Es NP-difícil, es decir, todos los problemas de NP pueden reducirse a él en tiempo polinómico.

Los problemas NP-completos son los problemas más representativos de la dificultad de la clase NP.

Vertex Cover es un problema NP-completo en su versión de decisión para grafos no dirigidos.

Esto significa que, si se encontrara un algoritmo polinómico para resolver todos los casos de Vertex Cover, también podrían resolverse en tiempo polinómico todos los problemas de NP.

### 8.6. Clase PSPACE

PSPACE contiene los problemas que pueden resolverse utilizando una cantidad de espacio de memoria polinómica respecto al tamaño de la entrada.

Un algoritmo puede tardar mucho tiempo y aun así pertenecer a PSPACE, siempre que el espacio utilizado esté limitado por una función polinómica.

Se cumple:

P ⊆ NP ⊆ PSPACE

### 8.7. Clases L y NL

La clase L contiene los problemas que pueden resolverse utilizando espacio logarítmico mediante una máquina de Turing determinista.

La clase NL contiene los problemas que pueden resolverse utilizando espacio logarítmico mediante una máquina de Turing no determinista.

Un ejemplo importante relacionado con NL es la alcanzabilidad en grafos dirigidos, conocida como Directed s-t Connectivity.

Este problema pregunta si existe una ruta dirigida desde un vértice s hasta un vértice t.

La alcanzabilidad dirigida es un problema NL-completo.

Esto permite relacionar directamente el módulo de alcanzabilidad de GraphLab TC con una de las clases fundamentales de complejidad espacial.

### 8.8. Intratabilidad

Un problema se considera intratable cuando no se conoce un algoritmo eficiente que lo resuelva para todas las entradas de tamaño general y su costo computacional resulta demasiado elevado al crecer la entrada.

Los problemas NP-completos son considerados candidatos importantes a la intratabilidad, aunque no se ha demostrado que ningún problema NP-completo requiera necesariamente tiempo superpolinómico.

La búsqueda exacta de Vertex Cover puede requerir examinar muchas combinaciones de vértices.

Por ejemplo, un método que analiza todos los subconjuntos de un conjunto de n vértices puede llegar a examinar:

2ⁿ subconjuntos.

Este crecimiento exponencial explica por qué la implementación de GraphLab TC limita la búsqueda exacta a grafos pequeños.

## 9. Relación de los fundamentos teóricos con GraphLab TC

GraphLab TC permite observar cómo los conceptos de grafos, algoritmos y complejidad se relacionan con problemas computacionales concretos.

| Fundamento | Aplicación en GraphLab TC |
|---|---|
| Conjuntos | Representación de vértices y aristas |
| Relaciones | Conexiones dirigidas entre vértices |
| Funciones | Operaciones y transiciones de los algoritmos |
| Algoritmos | Procedimientos BFS y DFS |
| Decidibilidad | Determinación de la existencia de una ruta |
| Clase P | Alcanzabilidad mediante BFS y DFS |
| Clase NP | Verificación de una solución de Vertex Cover |
| NP-completo | Clasificación teórica de Vertex Cover |
| Complejidad temporal | Análisis de operaciones de exploración |
| Complejidad espacial | Memoria utilizada por los algoritmos |

### 9.1. Alcanzabilidad y BFS

Breadth-First Search (BFS), o búsqueda en anchura, explora un grafo por niveles, utilizando una cola para administrar los vértices pendientes.

En grafos representados mediante listas de adyacencia, su complejidad temporal es:

O(V + E)

Donde:

- V representa la cantidad de vértices.
- E representa la cantidad de aristas.

Su complejidad espacial auxiliar es O(V).

En grafos no ponderados, BFS permite encontrar una ruta con la menor cantidad de aristas desde el origen hasta el destino.

### 9.2. Alcanzabilidad y DFS

Depth-First Search (DFS), o búsqueda en profundidad, explora un camino tanto como sea posible antes de retroceder.

Puede implementarse mediante una pila o recursividad.

Su complejidad temporal con listas de adyacencia es:

O(V + E)

Su complejidad espacial auxiliar es O(V).

DFS permite determinar si existe una ruta entre dos vértices, aunque no garantiza encontrar la ruta con menor cantidad de aristas.

### 9.3. Problema Vertex Cover

Vertex Cover es un problema de decisión definido sobre un grafo no dirigido.

Se busca determinar si existe un conjunto C de vértices que cubra todas las aristas y cuyo tamaño no supere un límite k.

Formalmente:

¿Existe C ⊆ V tal que |C| ≤ k y para toda arista {u, v} ∈ E se cumple que u ∈ C o v ∈ C?

La versión de decisión de Vertex Cover es NP-completa.

En GraphLab TC se utiliza una búsqueda exacta para instancias pequeñas y una función independiente para verificar las soluciones obtenidas.

La implementación interpreta las aristas del grafo como conexiones no dirigidas para este problema. Por tanto, la orientación original de una arista no cambia el criterio de cobertura.

El límite de 16 vértices es una restricción práctica de esta implementación, no una limitación teórica del problema.

## 10. Conclusiones

La Teoría de la Computación proporciona las bases matemáticas necesarias para comprender los modelos de cómputo, los lenguajes formales, los algoritmos y los límites de la resolución de problemas.

Los autómatas finitos permiten estudiar lenguajes regulares, mientras que las gramáticas libres de contexto y los autómatas de pila amplían la capacidad de reconocimiento. Las máquinas de Turing proporcionan un modelo general para estudiar la computabilidad y la decidibilidad.

Por otra parte, la teoría de complejidad permite clasificar los problemas según los recursos necesarios para resolverlos y verificarlos.

GraphLab TC integra estos fundamentos mediante la exploración de grafos dirigidos, la búsqueda de alcanzabilidad con BFS y DFS y el análisis del problema Vertex Cover.

El proyecto demuestra que no todos los problemas tienen la misma dificultad computacional: mientras que la alcanzabilidad puede resolverse en tiempo polinómico, Vertex Cover es NP-completo en su versión de decisión y requiere estrategias de búsqueda exacta costosas para instancias generales.

De esta manera, GraphLab TC funciona como una herramienta educativa para relacionar conceptos teóricos con su aplicación práctica en algoritmos y estructuras de datos.

## 11. Referencias bibliográficas

- Hopcroft, J. E., Motwani, R., & Ullman, J. D. (2006). *Introduction to Automata Theory, Languages, and Computation* (3rd ed.). Pearson.
- Sipser, M. (2013). *Introduction to the Theory of Computation* (3rd ed.). Cengage Learning.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
- Garey, M. R., & Johnson, D. S. (1979). *Computers and Intractability: A Guide to the Theory of NP-Completeness*. W. H. Freeman.
- Turing, A. M. (1936). On computable numbers, with an application to the Entscheidungsproblem. *Proceedings of the London Mathematical Society, 42*(1), 230–265.