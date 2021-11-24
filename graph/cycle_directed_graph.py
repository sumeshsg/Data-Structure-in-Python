def is_cycle_in_graph(graph, start):
    queue = list()
    queue.append(start)
    visited = list()
    while len(queue):
        node = queue.pop(0)
        if graph.get(node, None):
            for item in visited:
                if item in graph[node]:
                    return True
            queue.extend(graph[node])
            visited.append(node)
    return False


# graph = {"a": ["b", "c"],
#          "b": ["c", "d", "e"],
#          "c": ["d", "a"]
#          }

graph = {"a": ["b"],
         "b": ["c"],
         "c": ["d"]}
print(is_cycle_in_graph(graph, 'a'))
