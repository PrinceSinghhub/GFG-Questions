class Solution:

    # Function to return the minimum cost to reach the bottom right cell from the top left cell.
    def minimumCostPath(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        # Initialize the top-left cell with the starting point's cost
        dp[0][0] = grid[0][0]

        # Update the cell cost using only the top and left directions
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])

        # Update the cell cost using all four directions (top, bottom, left, right)
        for i in range(m):
            for j in range(n):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + grid[i][j])
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + grid[i][j])
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + grid[i][j])

        return dp[-1][-1]
