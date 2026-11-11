from .undirected_graph import add_edge

def receive_graph(file_path):
    graph={}

    file = open(file_path, "r")
    file.readline()

    for line in file:
        data = line.strip().split(",")
        source = int(data[0])
        target = int(data[1])
        weight = int(data[2])
        add_edge(graph, source, target, weight)

    file.close()
    return graph