def bfs(graph, start):
    result = []
    queue = list()
    queue.append(start)
    while len(queue):
        node = queue.pop(0)
        if graph.get(node, None) and node not in result:
            queue.extend(graph.get(node))
        result.append(node)
    return result


def dfs(graph, start):
    result = list()
    stack = list()
    stack.append(start)
    while len(stack):
        node = stack.pop()
        if graph.get(node) and node not in result:
            child_nodes = graph.get(node)
            stack.extend(child_nodes)
        result.append(node)
    return result


graph = {
    1: [2, 7, 8],
    2: [3, 6],
    3: [4, 5],
    8: [9, 12],
    9: [10, 11]

}
print(bfs(graph, 1))
print(dfs(graph, 1))
