import heapq


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
    graph[1].append(Edge(1, 3, 7))
    graph[1].append(Edge(1, 2, 1))
    graph[2].append(Edge(2, 4, 3))
    graph[3].append(Edge(3, 5, 1))
    graph[4].append(Edge(4, 3, 2))
    graph[4].append(Edge(4, 5, 5))


class Pair:
    def __init__(self, n, path):
        self.n = n
        self.path = path

    def __lt__(self, other):
        return self.path < other.path


def dijkstra(graph, src):
    pq = [Pair(src, 0)]
    dist = [float('inf')] * len(graph)
    vis = [False] * len(graph)
    dist[src] = 0

    while pq:
        curr = heapq.heappop(pq)
        if not vis[curr.n]:
            vis[curr.n] = True
            for i in range(len(graph[curr.n])):
                e = graph[curr.n][i]
                u, v, wt = e.src, e.dest, e.wt
                if not vis[v] and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, Pair(v, dist[v]))

    return dist


# Example usage:
V = 6
graph = [[] for _ in range(V)]
createGraph(graph)
src = 0
dist = dijkstra(graph, src)

for i in range(len(dist)):
    print(dist[i], end=" ")
