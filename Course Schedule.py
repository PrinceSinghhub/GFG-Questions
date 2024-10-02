from collections import deque


class Solution:
    def findOrder(self, n, m, pre):
        # Code here
        indeg = [0 for i in range(n)]
        adj = [[] for i in range(n)]
        for i in pre:
            indeg[i[0]] += 1
            adj[i[1]].append(i[0])
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        st = []
        c = 0
        while len(q):
            node = q.popleft()
            st.append(node)
            c += 1
            for curr in adj[node]:
                indeg[curr] -= 1
                if indeg[curr] == 0:
                    q.append(curr)
        if c == n:
            return st
        return []


# {
#  Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10 ** 6)


def check(graph, N, res):
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []

        for i in range(m):
            u, v = map(int, input().split())
            adj[v].append(u)
            prerequisites.append([u, v])

        ob = Solution()

        res = ob.findOrder(n, m, prerequisites)

        if (not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends