import sys

sys.setrecursionlimit(10 ** 6)
MAX = 40000
graph = [[] for i in range(MAX)]
graphT = [[] for i in range(MAX)]
sol = []
visited = [False for i in range(MAX)]
conne = [0 for i in range(MAX)]
ini = [0 for i in range(MAX)]


class Solution:
    def dfs(self, S):
        visited[S] = True
        for v in graph[S]:
            if (visited[v] == False):
                self.dfs(v)
        sol.append(S)

    def dfs2(self, S, C):
        visited[S] = False
        conne[S] = C
        for v in graphT[S]:
            if (visited[v]):
                self.dfs2(v, C)

    def captainAmerica(self, N, M, V):
        sol.clear()
        for i in range(1, N + 1):
            graph[i].clear()
            graphT[i].clear()
            visited[i] = False
            conne[i] = 0
            ini[i] = 0

        for i in range(M):
            u = V[i][0]
            v = V[i][1]
            graph[v].append(u)
            graphT[u].append(v)

        for i in range(1, N + 1):
            if (visited[i] == False):
                self.dfs(i)
        compon = 0
        for i in range(len(sol) - 1, 0, -1):
            if (visited[sol[i]]):
                compon = compon + 1
                self.dfs2(sol[i], compon)
                # compon = compon + 1
        lim = compon
        for i in range(1, N + 1):
            for j in range(len(graph[i])):
                if (conne[i] != conne[graph[i][j]]):
                    ini[conne[graph[i][j]]] = ini[conne[graph[i][j]]] + 1
        ou = 0
        for i in range(lim):
            if (ini[i] == 0):
                ou = ou + 1
        if (ou > 1):
            return 0
        ou = 0
        for i in range(1, N + 1):
            if (ini[conne[i]] == 0):
                ou = ou + 1
        return ou


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        V = list()
        for i in range(0, M):
            l = list(map(int, input().split()))
            V.append(l)
        ans = ob.captainAmerica(N, M, V);
        print(ans)

# } Driver Code Ends