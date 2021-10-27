def get_shortest_path(edges, start_node, end_node):
    graph = edge_to_graph(edges)
    if graph[start_node] and graph[end_node]:
        queue = [(start_node, 0)]
        visited = set()
        while len(queue) > 0:
            node, distance = queue.pop(0)
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return distance
            else:
                for new_node in graph.get(node):
                    queue.append((new_node, distance + 1))
    else:
        return None


def edge_to_graph(edges):
    graph = {}
    for edge in edges:
        node_1 = edge[0]
        node_2 = edge[1]
        if not graph.get(node_1, None):
            graph[node_1] = []
        if not graph.get(node_2, None):
            graph[node_2] = []
        graph[node_1].append(node_2)
        graph[node_2].append(node_1)
    return graph


edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]

# graph = {"w": ["x", "y"],
#          "x": ["w", "y"],
#          "v": ["w", "z"],
#          "y": ["x", "z"],
#          "z": ["y", "v"]
#          }
print(get_shortest_path(edges, "w", "z"))
