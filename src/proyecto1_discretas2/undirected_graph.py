def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = {}


def add_edge(graph, source, target, weight):
    add_vertex(graph, source)
    add_vertex(graph, target)
    graph[source][target] = weight
    graph[target][source] = weight