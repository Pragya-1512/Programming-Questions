class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1, 1))
    graph[0].append(Edge(0, 2, 1))
    graph[1].append(Edge(1, 0, 1))
    graph[1].append(Edge(1, 3, 1))
    graph[2].append(Edge(2, 0, 1))
    graph[2].append(Edge(2, 4, 1))
    graph[3].append(Edge(3, 1, 1))
    graph[3].append(Edge(3, 4, 1))
    graph[3].append(Edge(3, 5, 1))
    graph[4].append(Edge(4, 2, 1))
    graph[4].append(Edge(4, 3, 1))
    graph[4].append(Edge(4, 5, 1))
    graph[5].append(Edge(5, 3, 1))
    graph[5].append(Edge(5, 4, 1))
    graph[5].append(Edge(5, 6, 1))
    graph[5].append(Edge(6, 5, 1))


def dfs(graph, curr, visited):
    if visited[curr]:
        return

    print(curr, end=" ")
    visited[curr] = True

    for e in graph[curr]:
        dfs(graph, e.dest, visited)


# Example usage:
V = 7
graph = [[] for _ in range(V)]
createGraph(graph)
dfs(graph, 0, [False] * V)
