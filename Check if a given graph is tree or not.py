# User function Template for python3
from collections import deque


class Solution:
    def isTree(self, n, m, adj):
        adj_list = [[] for _ in range(n)]

        for edge in adj:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        vis = [False] * n
        q = deque([(0, -1)])
        vis[0] = True

        while q:
            node, parent = q.popleft()

            for neighbor in adj_list[node]:
                if not vis[neighbor]:
                    vis[neighbor] = True
                    q.append((neighbor, node))
                elif neighbor != parent:
                    return 0

        for visited in vis:
            if not visited:
                return 0

        return 1


# {
# Driver Code Starts
# Initial Template for Python 3

for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append([a, b])

    ob = Solution()
    print(ob.isTree(n, m, edges))
# } Driver Code Ends