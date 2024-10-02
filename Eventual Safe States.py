# User function Template for python3

from typing import List
from collections import deque


class Solution:
    def eventualSafeNodes(self, V: int, adj: List[List[int]]) -> List[int]:
        adj_rev = [[] for _ in range(V)]
        indegree = [0] * V

        for i in range(V):
            for it in adj[i]:
                adj_rev[it].append(i)
                indegree[i] += 1

        ans = []
        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            ans.append(node)

            for nbr in adj_rev[node]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    q.append(nbr)

        ans.sort()
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())
    for t in range(T):2

        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end=' ')
        print()

# } Driver Code Ends