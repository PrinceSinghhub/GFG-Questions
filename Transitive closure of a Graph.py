from itertools import product


class Solution:
    def transitiveClosure(self, N, graph):
        for k, i, j in product(range(N), range(N), range(N)):
            graph[i][i] = 1
            if graph[i][k] and graph[k][j]: graph[i][j] = 1

        return graph