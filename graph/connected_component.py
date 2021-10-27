def get_connected_component(graph):
    visited = set()
    count = 0
    for node, _ in graph.items():
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, node, visited):
    if node in visited:
        return False
    if graph.get(node):
        visited.add(node)
        for new_nod in graph.get(node):
            explore(graph, new_nod, visited)
    return True


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    4: [3, 2],
    100: [200, 300]

}

print(get_connected_component(graph))
