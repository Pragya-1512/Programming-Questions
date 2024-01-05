from collections import defaultdict, deque


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 2))
    graph[0].append(Edge(0, 3))
    graph[1].append(Edge(1, 0))
    graph[2].append(Edge(2, 1))
    graph[3].append(Edge(3, 4))


def topSort(graph, curr, stack, vis):
    vis[curr] = True
    for e in graph[curr]:
        if not vis[e.dest]:
            topSort(graph, e.dest, stack, vis)
    stack.append(curr)


def dfs(graph, vis, curr):
    vis[curr] = True
    print(curr, end=" ")
    for e in graph[curr]:
        if not vis[e.dest]:
            dfs(graph, vis, e.dest)


def kosaraju(graph, V):
    # Step 1
    stack = []
    vis = [False] * V
    for i in range(V):
        if not vis[i]:
            topSort(graph, i, stack, vis)

    # Step 2
    transpose = [[] for _ in range(V)]
    for i in range(V):
        vis[i] = False
        for j in range(len(graph[i])):
            e = graph[i][j]
            transpose[e.dest].append(Edge(e.dest, e.src))

    # Step 3
    while stack:
        curr = stack.pop()
        if not vis[curr]:
            print("SCC :", end=" ")
            dfs(transpose, vis, curr)
            print()


# Example usage:
V = 5
graph = [[] for _ in range(V)]
createGraph(graph)
kosaraju(graph, V)
