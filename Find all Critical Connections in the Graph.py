#User function Template for python3

class Solution:
    def __init__(self):
        self.ans = []
        self.timer = 0
        self.vis = []
        self.first = []
        self.low = []

    def dfs(self, cur, par, adj):
        self.vis[cur] = True
        self.first[cur] = self.low[cur] = self.timer
        self.timer += 1

        for ch in adj[cur]:
            if ch == par:
                continue
            if self.vis[ch]:
                self.low[cur] = min(self.low[cur], self.first[ch])
            else:
                self.dfs(ch, cur, adj)
                self.low[cur] = min(self.low[cur], self.low[ch])
                if self.low[ch] > self.first[cur]:
                    self.ans.append([min(ch, cur), max(ch, cur)])

    def criticalConnections(self, n, adj):
        self.timer = 0
        self.vis = [False] * n
        self.first = [-1] * n
        self.low = [-1] * n

        for i in range(n):
            if not self.vis[i]:
                self.dfs(i, -1, adj)

        self.ans.sort()
        return self.ans

#{
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends