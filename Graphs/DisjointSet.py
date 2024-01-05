class DisjointSets:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def find_number_of_provinces(is_connected):
    n = len(is_connected)
    ds = DisjointSets(n)

    for i in range(n):
        for j in range(n):
            if is_connected[i][j] == 1:
                ds.union(i, j)

    provinces = set()
    for i in range(n):
        provinces.add(ds.find(i))

    return len(provinces)


# Example usage:
connections = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

num_provinces = find_number_of_provinces(connections)
print("Number of provinces:", num_provinces)
