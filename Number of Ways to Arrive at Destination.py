# User function Template for python3

from typing import List
from collections import defaultdict
import sys


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for i, j, k in roads:
            d[i].append([j, k])
            d[j].append([i, k])

        q, t, c = [[0, 0]], float('inf'), 0
        v = [float('inf')] * (n)
        while q:
            node, dis = q.pop(0)
            for cnode, cdis in d[node]:
                if cnode == n - 1:
                    if cdis + dis == v[cnode]:
                        c += 1
                    elif cdis + dis < v[cnode]:
                        v[cnode] = cdis + dis
                        c = 1
                else:
                    if v[cnode] >= dis + cdis:
                        v[cnode] = dis + cdis
                        q.append([cnode, dis + cdis])
        return c


# {
# Driver Code Starts
# Initial Template for Python 3

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        adj = []

        for i in range(m):
            tmp = []
            x, y, z = map(int, input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)

        obj = Solution()
        res = obj.countPaths(n, adj)

        print(res)

# } Driver Code Ends