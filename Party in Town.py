class Solution:
    def partyHouse(self, N, adj):
        # code here
        # find distance of each node from each node and then calculate the minimum of all the maximums
        def dfs(curr, prev, dep):
            maxdep[0] = max(maxdep[0], dep)
            for edge in adj[curr]:
                if edge != prev:
                    dfs(edge, curr, dep + 1)

        ans = 999999999
        for i in range(1, N + 1):
            maxdep = [0]
            dfs(i, -1, 0)
            ans = min(ans, maxdep[0])
        return ans

ans = Solution()
n = 4
arr = [[1,2],[2,3],[2,4]]

rot = [[2],[1,3,4],[2],[2]]
print(ans.partyHouse(n-1,arr))