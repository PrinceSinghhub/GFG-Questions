class Solution:
    def minColour(self, N, M, mat):
        adj = [[] for _ in range(N + 1)]
        visit = [False] * (N + 1)
        dist = [0] * (N + 1)

        for u, v in mat:
            adj[u].append(v)

        for i in range(1, N + 1):
            if not visit[i]:
                self.dfs(i, adj, visit, dist)

        return max(dist)

    def dfs(self, x, adj, visit, dist):
        visit[x] = True
        chain_len = 0

        for v in adj[x]:
            if not visit[v]:
                self.dfs(v, adj, visit, dist)
            chain_len = max(chain_len, dist[v])

        dist[x] = chain_len + 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        mat = [[0] * 2 for y in range(M)]
        for i in range(M):
            arr = input().split()
            mat[i][0] = int(arr[0])
            mat[i][1] = int(arr[1])

        ob = Solution()
        print(ob.minColour(N, M, mat))
# } Driver Code Ends