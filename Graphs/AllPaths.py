class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 2))
    graph[1].append(Edge(1, 0))
    graph[1].append(Edge(1, 3))
    graph[2].append(Edge(2, 0))
    graph[2].append(Edge(2, 4))
    graph[3].append(Edge(3, 1))
    graph[3].append(Edge(3, 4))
    graph[3].append(Edge(3, 5))
    graph[4].append(Edge(4, 2))
    graph[4].append(Edge(4, 3))
    graph[4].append(Edge(4, 5))
    graph[5].append(Edge(5, 3))
    graph[5].append(Edge(5, 4))
    graph[5].append(Edge(5, 6))
    graph[6].append(Edge(6, 5))


def printAllPaths(graph, src, tar, path, vis):
    if src == tar:
        print(path)
        return

    for e in graph[src]:
        if not vis[e.dest]:
            vis[e.dest] = True
            printAllPaths(graph, e.dest, tar, path + "->" + str(e.dest), vis)
            vis[e.dest] = False


# Example usage:
V = 7
graph = [[] for _ in range(V)]
createGraph(graph)
src = 0
tar = 5
vis = [False] * V
vis[src] = True
printAllPaths(graph, src, tar, str(src), vis)
