class Solution:
    def isEularCircuitExist(self, v, adj):

        for i in range(v):
            if len(adj[i]) % 2:
                return 0
        return 1