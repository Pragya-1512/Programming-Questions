class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1, 2))
    graph[0].append(Edge(0, 2, 4))
    graph[1].append(Edge(1, 2, -4))
    graph[2].append(Edge(2, 3, 2))
    graph[3].append(Edge(3, 4, 4))
    graph[4].append(Edge(4, 1, -1))


def bellmanFord(graph, src):
    V = len(graph)
    dist = [float('inf')] * V
    dist[src] = 0

    # Relax edges |V| - 1 times
    for _ in range(V - 1):
        for j in range(V):
            for k in range(len(graph[j])):
                e = graph[j][k]
                u, v, wt = e.src, e.dest, e.wt
                if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

    # Detecting Negative Weight Cycle
    for j in range(V):
        for k in range(len(graph[j])):
            e = graph[j][k]
            u, v, wt = e.src, e.dest, e.wt
            if dist[u] != float('inf') and dist[u] + wt < dist[v]:
                print("Negative weight cycle exists")
                return

    for i in range(V):
        print(dist[i], end=" ")
    print()


# Example usage:
V = 5
graph = [[] for _ in range(V)]
createGraph(graph)
src = 0
bellmanFord(graph, src)
