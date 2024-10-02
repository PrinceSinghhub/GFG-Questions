# User function Template for python3

import collections
from collections import deque
from collections import defaultdict


class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        visited = set()

        def dfs(n, ns, edges):
            nonlocal visited
            ns.add(n)
            visited.add(n)
            for nbr in adj[n]:
                edges.add((min(n, nbr), max(n, nbr)))
                if nbr not in ns:
                    dfs(nbr, ns, edges)

        ans = 0
        for n in range(1, V + 1):
            if n not in visited:
                ns = set()
                edges = set()
                dfs(n, ns, edges)
                nv = len(ns)
                ne = len(edges)
                if nv * (nv - 1) // 2 == ne:
                    ans += 1
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

from sys import stdin, stdout

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V + 1)]
        for _ in range(E):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends