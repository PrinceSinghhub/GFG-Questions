class Solution:
    def dfs(self, node, lev, vis, adj, X):
        if node == X:
            return lev
        vis[node] = 1

        for it in adj[node]:
            if not vis[it]:
                level = self.dfs(it, lev + 1, vis, adj, X)
                if level != -1:
                    return level

        return -1

    # Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        vis = [0] * V
        return self.dfs(0, 0, vis, adj, X)