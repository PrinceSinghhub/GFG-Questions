from collections import defaultdict, deque


class Solution:
    def shortestPath(self, edges, N, M, src):
        adj = defaultdict(list)

        for i in range(M):
            u = edges[i][0]
            v = edges[i][1]
            adj[u].append(v)
            adj[v].append(u)

        ans = [-1] * N
        ans[src] = 0
        q = deque([src])

        while q:
            temp = q.popleft()
            for i in adj[temp]:
                if ans[i] == -1:
                    ans[i] = ans[temp] + 1
                    q.append(i)

        return ans