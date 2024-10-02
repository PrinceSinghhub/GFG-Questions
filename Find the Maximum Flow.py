class Solution:
    def solve(self, N, M, Edges):
        graph = []
        for _ in range(N + 1):
            graph.append([0] * (N + 1))

        for edge in Edges:
            graph[edge[0]][edge[1]] += edge[2]
            graph[edge[1]][edge[0]] += edge[2]

        max_flow = 0
        parent = [None] * (N + 1)

        while self.bfs(graph, N, parent):
            v = N
            flow = float('inf')
            while v != 1:
                flow = min(flow, graph[parent[v]][v])
                v = parent[v]

            max_flow += flow

            v = N
            while v != 1:
                graph[parent[v]][v] -= flow
                graph[v][parent[v]] += flow
                v = parent[v]

        return max_flow

    def bfs(self, graph, N, parent):
        Q = [1]
        is_visited = [False] * (N + 1)
        is_visited[1] = True
        while len(Q) != 0:
            u = Q.pop(0)

            for v in range(1, N + 1):
                w = graph[u][v]
                if is_visited[v] == False and w > 0:
                    parent[v] = u
                    is_visited[v] = True
                    Q.append(v)
                    if v == N:
                        return True

        return False