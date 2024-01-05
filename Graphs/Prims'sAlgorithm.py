import heapq


class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def createGraph(graph):
    for i in range(len(graph)):
        graph[i] = []

    graph[0].append(Edge(0, 1, 10))
    graph[0].append(Edge(0, 2, 15))
    graph[0].append(Edge(0, 3, 30))
    graph[1].append(Edge(1, 0, 10))
    graph[1].append(Edge(1, 3, 40))
    graph[2].append(Edge(2, 0, 15))
    graph[2].append(Edge(2, 3, 50))
    graph[3].append(Edge(3, 1, 40))
    graph[3].append(Edge(3, 2, 50))


class Pair:
    def __init__(self, v, wt):
        self.v = v
        self.wt = wt

    def __lt__(self, other):
        return self.wt < other.wt


def primAlgo(graph):
    vis = [False] * len(graph)
    pq = [Pair(0, 0)]
    cost = 0

    while pq:
        curr = heapq.heappop(pq)
        if not vis[curr.v]:
            vis[curr.v] = True
            cost += curr.wt
            for i in range(len(graph[curr.v])):
                e = graph[curr.v][i]
                if not vis[e.dest]:
                    heapq.heappush(pq, Pair(e.dest, e.wt))

    print(cost)


# Example usage:
V = 4
graph = [[] for _ in range(V)]
createGraph(graph)
primAlgo(graph)
