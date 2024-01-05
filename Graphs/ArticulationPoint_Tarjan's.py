from collections import defaultdict


class Edge:
    def __init__(self, dest):
        self.dest = dest


def dfs(graph, curr, par, vis, dt, low, time, isArticulation):
    vis[curr] = True
    dt[curr] = low[curr] = time[0]
    child = 0

    for e in graph[curr]:
        if e.dest == par:
            continue
        if vis[e.dest]:
            low[curr] = min(low[curr], dt[e.dest])
        else:
            dfs(graph, e.dest, curr, vis, dt, low, time, isArticulation)
            low[curr] = min(low[curr], low[e.dest])
            if dt[curr] <= low[e.dest] and par != -1:
                isArticulation[curr] = True
            child += 1

    if par == -1 and child > 1:
        isArticulation[curr] = True

    time[0] += 1


def getArticulation(graph, V):
    dt = [0] * V
    low = [0] * V
    time = [0]
    vis = [False] * V
    isArticulation = [False] * V

    for i in range(V):
        if not vis[i]:
            dfs(graph, i, -1, vis, dt, low, time, isArticulation)

    result = [i for i in range(V) if isArticulation[i]]
    return result


# Example usage:
V = 5
graph = defaultdict(list)
edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 4], [4, 2]]
for u, v in edges:
    graph[u].append(Edge(v))
    graph[v].append(Edge(u))

articulation_points = getArticulation(graph, V)
print("Articulation Points:")
print(articulation_points)
