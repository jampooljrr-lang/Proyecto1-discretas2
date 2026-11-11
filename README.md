# Proyecto 1 - Matemáticas Discretas II

Proyecto desarrollado en Python para la asignatura Matemáticas Discretas II de la Universidad del Valle.

Joseth Jampool Rodriguez Rosero - 2537119

## Descripción

Este proyecto consiste en implementar algunas operaciones básicas con grafos, utilizando Python y sin depender de librerías especializadas en grafos.

En esta primera entrega trabajé principalmente con la representación de grafos dirigidos y no dirigidos mediante listas de adyacencia, además de la lectura de archivos CSV para construir grafos a partir de sus conexiones.

El proyecto está desarrollado con programación imperativa y funciones, ya que es la forma de programar con la que tengo más familiaridad actualmente.

## Tecnologías utilizadas

- **Python 3.13:** lenguaje de programación.
- **UV:** administración del proyecto y del entorno de Python.
- **Git:** control de versiones.
- **GitHub:** almacenamiento del código y seguimiento de cambios.
- **Visual Studio Code:** editor de código.

No se utilizaron librerías especializadas en grafos.

## Estructura del proyecto

```text
Proyecto1-discretas2/
│
├── reading_files/
│   ├── ejemplo_1.csv
│   ├── ejemplo_2.csv
│   ├── ejemplo_3.csv
│   ├── ejemplo_4.csv
│   ├── ejemplo_5.csv
│   └── ejemplo_6.csv
│
├── src/
│   └── proyecto1_discretas2/
│       ├── __init__.py
│       ├── undirected_graph.py
│       ├── directed_graph.py
│       └── reader.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

## Funcionalidades implementadas

### Grafos no dirigidos

En `undirected_graph.py` implementé dos funciones:

- `add_vertex()`: agrega un vértice al grafo cuando todavía no existe.
- `add_edge()`: conecta dos vértices y almacena el peso de la arista.

Como se trata de un grafo no dirigido, las conexiones se guardan en ambos sentidos.

### Grafos dirigidos

En `directed_graph.py` implementé `add_directed_edge()`.

Esta función agrega conexiones que tienen una dirección específica. A diferencia del grafo no dirigido, no se guarda automáticamente la conexión contraria.

### Lectura de archivos

En `reader.py` implementé `receive_graph()`.

La función recibe la ruta de un archivo CSV, lee sus filas y construye un grafo no dirigido utilizando las conexiones y los pesos encontrados.

Los archivos deben tener el siguiente formato:

```csv
source,target,weight
1,2,4
1,3,2
```

Para leerlos utilicé funciones básicas de Python, como `open()`, `readline()` y `split()`.

## Instalación y uso

Para ejecutar el proyecto es necesario tener UV instalado.

Desde la carpeta principal del proyecto se puede abrir Python mediante:

```bash
uv run python
```

### Ejemplo de uso: grafo no dirigido

```python
from proyecto1_discretas2.undirected_graph import add_vertex, add_edge

graph = {}

add_vertex(graph, 1)
add_edge(graph, 1, 2, 7)

print(graph)
```

Resultado:

```text
{1: {2: 7}, 2: {1: 7}}
```

### Ejemplo de uso: grafo dirigido

```python
from proyecto1_discretas2.directed_graph import add_directed_edge

graph = {}

add_directed_edge(graph, 1, 2, 7)

print(graph)
```

Resultado:

```text
{1: {2: 7}, 2: {}}
```

### Leer un archivo CSV

```python
from proyecto1_discretas2.reader import receive_graph

graph = receive_graph("reading_files/ejemplo_1.csv")

print(graph)
```

Esta instrucción lee el archivo y muestra el grafo construido.

Las rutas de los archivos de ejemplo son relativas a la carpeta principal del proyecto.

## Estado del proyecto

Esta es una entrega parcial.

Se implementaron las representaciones básicas de grafos dirigidos y no dirigidos, la creación de vértices y aristas con pesos y la lectura de archivos CSV para grafos no dirigidos.

Quedaron pendientes las funciones para:

- Verificar si un grafo es conexo.
- Detectar ciclos.
- Determinar si un grafo es un árbol.
- Determinar si un grafo es un bosque.

Estas funcionalidades requieren trabajar con algoritmos de recorrido que todavía necesito reforzar.

Me queda como objetivo mejorar mi lógica de programación y entender mejor los algoritmos de recorrido de grafos para poder completar este tipo de ejercicios con mayor independencia.

## Proceso de desarrollo y dificultades

Se me dificultó comprender cómo funcionaban los diccionarios anidados para almacenar los vértices, sus vecinos y los pesos.

A medida que fui haciendo pruebas, logré comprender mejor cómo se agregan las conexiones y por qué los grafos dirigidos y no dirigidos necesitan un tratamiento diferente.

Para la lectura de archivos preferí utilizar instrucciones básicas como `open()` y `split()`, porque me resultaron más fáciles de entender.

Aunque no alcancé a completar todos los puntos, el proyecto me permitió practicar Python y conocer herramientas de desarrollo que antes no manejaba muy bien.

## Uso de inteligencia artificial

Durante el desarrollo utilicé IA para aprender a configurar UV, trabajar con Git y GitHub, interpretar errores de la terminal y realizar pruebas.

En algunas partes recibí ejemplos de código y soluciones que adapté o utilicé para avanzar. También usé sugerencias del editor mientras escribía código.

Este README fue organizado con ayuda de IA, tomando como base el trabajo realizado y las dificultades que tuve durante el desarrollo.

Reconozco que todavía necesito practicar más para poder desarrollar por mi cuenta los algoritmos que quedaron pendientes.