class Solution:
    def dfs(self, g, i, j):
        if i < 0 or j < 0 or i > len(g) - 1 or j > len(g[i]) - 1 or g[i][j] == 0:
            return 0
        self.count = self.count + 1
        g[i][j] = 0
        self.dfs(g, i + 1, j)
        self.dfs(g, i - 1, j)
        self.dfs(g, i, j + 1)
        self.dfs(g, i, j - 1)
        self.dfs(g, i + 1, j + 1)
        self.dfs(g, i + 1, j - 1)
        self.dfs(g, i - 1, j + 1)
        self.dfs(g, i - 1, j - 1)

        def findMaxArea(self, grid):
            if not grid:

                return 0
            ans = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    self.count = 0
                    self.dfs(grid, i, j)
                    ans = max(ans, self.count)
            return ans


# {
# Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends