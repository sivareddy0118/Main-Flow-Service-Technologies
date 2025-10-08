# Detect cycle in an undirected graph using DFS

def has_cycle(graph, node, visited, parent):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True
    return False

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

visited = [False] * len(graph)
print("Graph contains cycle?", has_cycle(graph, 0, visited, -1))
