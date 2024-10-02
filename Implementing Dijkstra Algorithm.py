import heapq


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V, adj, S):
        # code here

        l = [] * (V + 1)
        dis = [float('inf')] * (V)
        dis[S] = 0
        heapq.heappush(l, (0, S))

        while l:
            di, curr = heapq.heappop(l)

            for i in adj[curr]:
                nextdis = i[1]
                nextcurr = i[0]
                if di + nextdis < dis[nextcurr]:
                    dis[nextcurr] = di + nextdis
                    heapq.heappush(l, (dis[nextcurr], nextcurr))

        return dis


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends