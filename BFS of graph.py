from typing import List
from queue import Queue


class Solution:

    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visit = [0 for i in range(V)]
        ans = [0]
        q = [0]
        visit[0] = 1
        while len(q) != 0:
            j = 0
            curr = q[0]
            q.remove(q[0])
            while j < len(adj[curr]):
                if adj[curr][j] != None and visit[adj[curr][j]] != 1:
                    ans.append(adj[curr][j])
                    visit[adj[curr][j]] = 1
                    q.append(adj[curr][j])
                j += 1
        return ans


# {
# Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()

# } Driver Code Ends