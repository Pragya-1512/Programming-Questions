class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 2))
    graph[1].append(Edge(1, 0))
    graph[2].append(Edge(2, 3))
    graph[3].append(Edge(3, 0))


def isCyclicUtil(graph, curr, vis, stack):
    vis[curr] = True
    stack[curr] = True

    for e in graph[curr]:
        if stack[e.dest]:  # Cycle exists
            return True
        elif not vis[e.dest] and isCyclicUtil(graph, e.dest, vis, stack):
            return True

    stack[curr] = False
    return False

# O(V + E)


def isCyclic(graph):
    vis = [False] * len(graph)

    for i in range(len(graph)):
        if not vis[i]:
            cycle = isCyclicUtil(graph, i, vis, [False] * len(vis))
            if cycle:
                return True

    return False


# Example usage:
V = 4
graph = [[] for _ in range(V)]
createGraph(graph)
print(isCyclic(graph))
