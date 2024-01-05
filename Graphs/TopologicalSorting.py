from collections import defaultdict


class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[2].append(Edge(2, 3))
    graph[3].append(Edge(3, 1))
    graph[4].append(Edge(4, 0))
    graph[4].append(Edge(4, 1))
    graph[5].append(Edge(5, 0))
    graph[5].append(Edge(5, 2))


def topoSortUtil(graph, curr, vis, stack):
    vis[curr] = True
    for i in range(len(graph[curr])):
        e = graph[curr][i]
        if not vis[e.dest]:
            topoSortUtil(graph, e.dest, vis, stack)
    stack.append(curr)

# O(V+E)


def topoSort(graph):
    vis = [False] * len(graph)
    stack = []

    for i in range(len(graph)):
        if not vis[i]:
            topoSortUtil(graph, i, vis, stack)

    while stack:
        print(stack.pop(), end=" ")


# Example usage:
V = 6
graph = defaultdict(list)
createGraph(graph)
topoSort(graph)
