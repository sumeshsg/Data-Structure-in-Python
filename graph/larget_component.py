def get_largest_component(graph):
    largest_component_node_count = 0
    visited = set()
    for node, _ in graph.items():
        cnt = explore(graph, node, visited)
        largest_component_node_count = max(cnt, largest_component_node_count)
    return largest_component_node_count


def explore(graph, node, visited):
    if node in visited:
        return 0
    cnt = 1
    if graph.get(node, None):
        visited.add(node)
        for new_node in graph[node]:
            cnt += explore(graph, new_node, visited)
    return cnt


graph = {
    0: [8, 1, 5, 800],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    4: [3, 2],
    100: [200, 300]

}

print(get_largest_component(graph))
