class Solution:
    def biGraph(self, arr, n, e):
        adj = [[] for _ in range(n)]
        for i in range(e):
            adj[arr[2 * i]].append(arr[2 * i + 1])
            adj[arr[2 * i + 1]].append(arr[2 * i])
        parent = [-1] * n
        visited = [True] + [False] * (n - 1)
        depth = [0] + [-1] * (n - 1)
        lowpoint = [0] + [-1] * (n - 1)
        stack = [0]
        while stack:
            node = stack[-1]
            pop = True
            for i, node2 in enumerate(adj[node]):
                if node2 != parent[node] and not visited[node2]:
                    if node == 0 and i > 0:
                        return 0
                    visited[node2] = True
                    pop = False
                    stack.append(node2)
                    parent[node2] = node
                    depth[node2] = depth[node] + 1
                    lowpoint[node2] = lowpoint[node] + 1
                    break
            if pop:
                for node2 in adj[node]:
                    if parent[node2] == node and lowpoint[node2] >= depth[node] and len(stack) >= 2:
                        return 0
                    if node2 != parent[node]:
                        lowpoint[node] = min(lowpoint[node], lowpoint[node2])
                stack.pop()
        for i in range(n):
            if not visited[i]:
                return 0
        return 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, e = map(int, input().split())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.biGraph(arr, n, e))