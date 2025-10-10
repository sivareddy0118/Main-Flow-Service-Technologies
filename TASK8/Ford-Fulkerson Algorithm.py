# Ford-Fulkerson Algorithm to find Maximum Flow
from collections import deque

def bfs(capacity, s, t, parent):
    visited = [False] * len(capacity)
    queue = deque([s])
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v, cap in enumerate(capacity[u]):
            if not visited[v] and cap > 0:
                parent[v] = u
                visited[v] = True
                queue.append(v)
                if v == t:
                    return True
    return False

def ford_fulkerson(capacity, source, sink):
    parent = [-1] * len(capacity)
    max_flow = 0
    while bfs(capacity, source, sink, parent):
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = parent[v]
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        max_flow += path_flow
    return max_flow

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

print("Maximum Flow:", ford_fulkerson(graph, 0, 5))
