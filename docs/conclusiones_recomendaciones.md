# Conclusiones y recomendaciones
## Proyecto GraphLab TC-UNAH

## 1. Conclusiones

1. El desarrollo de GraphLab TC-UNAH permitió aplicar conceptos de Teoría de la Computación mediante una herramienta interactiva enfocada en la creación, exploración y análisis de grafos. De esta manera, se relacionaron los fundamentos teóricos con su implementación práctica.

2. La implementación de los algoritmos BFS y DFS permitió estudiar dos estrategias diferentes de recorrido de grafos. Aunque ambos pueden determinar la alcanzabilidad entre vértices, se diferencian en su forma de exploración: BFS trabaja por niveles y permite encontrar rutas con el menor número de aristas en grafos no ponderados, mientras que DFS profundiza en una rama antes de explorar otras alternativas.

3. La incorporación del problema Vertex Cover amplió el alcance del proyecto al introducir un problema de decisión relacionado con la complejidad computacional. Su implementación permitió experimentar con la búsqueda de coberturas de vértices y comprender por qué los problemas NP-completos requieren especial atención cuando aumenta el tamaño de la entrada.

4. La arquitectura modular permitió separar las responsabilidades del sistema entre la administración de grafos, los algoritmos, la interfaz, las visualizaciones y las pruebas. Esta organización facilita la comprensión del código y permite realizar futuras mejoras sin tener que modificar toda la aplicación.

5. Las visualizaciones interactivas contribuyeron a representar los grafos y facilitar la comprensión de sus conexiones y recorridos. Esto convierte la aplicación en un recurso de apoyo para estudiar los procedimientos implementados.

6. La ejecución de la suite de pruebas automatizadas produjo un resultado de 48 pruebas aprobadas y ningún fallo en la ejecución realizada el 25 de noviembre de 2026. Este resultado respalda el funcionamiento de los componentes cubiertos por dichas pruebas.

7. El proyecto permitió relacionar conceptos como alcanzabilidad, algoritmos de exploración, problemas de decisión, complejidad temporal y problemas NP-completos, demostrando la importancia de la Teoría de la Computación en el análisis y desarrollo de soluciones informáticas.

## 2. Recomendaciones

1. Ampliar las funcionalidades del editor para incorporar nuevas opciones de creación y modificación de grafos, incluyendo otras formas de representación.

2. Incorporar algoritmos adicionales de grafos, como Dijkstra para grafos ponderados, detección de ciclos y búsqueda de componentes conexas, cuando se amplíe el alcance del proyecto.

3. Mejorar el análisis experimental de BFS y DFS mediante pruebas con grafos de diferentes tamaños y estructuras, registrando los tiempos de ejecución y el consumo de memoria bajo condiciones controladas.

4. Explorar estrategias de optimización para Vertex Cover, como algoritmos aproximados, poda de búsqueda y técnicas de ramificación y acotamiento, para estudiar instancias de mayor tamaño.

5. Ampliar los casos de prueba para cubrir nuevas situaciones, entradas inválidas y escenarios de integración entre los módulos.

6. Mantener actualizada la documentación técnica y teórica para facilitar el mantenimiento del sistema y permitir que otros estudiantes comprendan su funcionamiento.

7. Utilizar GraphLab TC como herramienta complementaria de aprendizaje, acompañando las demostraciones prácticas con el estudio de los fundamentos matemáticos y de complejidad computacional.

## 3. Consideración final

GraphLab TC-UNAH constituye una aplicación educativa que integra fundamentos de Teoría de la Computación con herramientas de programación y visualización. Su desarrollo permitió transformar conceptos abstractos en experiencias prácticas de exploración y análisis, fortaleciendo la comprensión de los grafos, la alcanzabilidad y los problemas de decisión.