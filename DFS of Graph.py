# User function Template for python3

class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        result = []

        def dfs(vertex):
            visited[vertex] = True
            result.append(vertex)
            for neighbour in adj[vertex]:
                if not visited[neighbour]:
                    dfs(neighbour)

        for v in range(V):
            if not visited[v]:
                dfs(v)
        return result


# {
# Driver Code Starts

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V + 1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
# } Driver Code Ends