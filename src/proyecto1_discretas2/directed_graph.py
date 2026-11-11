
from .undirected_graph import add_vertex

def add_directed_edge(graph, source, target, weight):
    add_vertex(graph, source)
    add_vertex(graph, target)
    
    graph[source][target] = weight
