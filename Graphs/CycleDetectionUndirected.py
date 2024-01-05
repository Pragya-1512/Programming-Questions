class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 2))
    graph[0].append(Edge(0, 3))
    graph[1].append(Edge(1, 0))
    graph[1].append(Edge(1, 2))
    graph[2].append(Edge(2, 0))
    graph[2].append(Edge(2, 1))
    graph[3].append(Edge(3, 0))
    graph[3].append(Edge(3, 4))
    graph[4].append(Edge(4, 3))


def isCyclicUtil(graph, vis, curr, par):
    vis[curr] = True
    for e in graph[curr]:
        # case 1
        if vis[e.dest] and e.dest != par:
            isCycle = isCyclicUtil(graph, vis, e.dest, curr)
            if isCycle:
                return True
        # case 2
        elif e.dest == par:
            continue
        # case 3
        else:
            return True
    return False

# O(V + E)


def isCyclic(graph, vis):
    for i in range(len(graph)):
        if not vis[i]:
            if isCyclicUtil(graph, vis, i, -1):
                return True
    return False


# Example usage:
V = 5
graph = [[] for _ in range(V)]
createGraph(graph)
print(isCyclic(graph, [False] * V))
