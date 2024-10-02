from typing import List

class Solution:
    def dfs(self, s, adj, vis, candies):
        vis[s] = 1
        for it in adj[s]:
            candies[it] = max(candies[it], candies[s] + 1)
            self.dfs(it, adj, vis, candies)

    def minCandy(self, n, ratings):
        # code here
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            if ratings[i-1] > ratings[i]:
                adj[i].append(i-1)
            elif ratings[i-1] < ratings[i]:
                adj[i-1].append(i)

        vis = [0] * n
        candies = [1] * n
        for i in range(n):
            if not vis[i]:
                self.dfs(i, adj, vis, candies)

        return sum(candies)