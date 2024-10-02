class Solution:
    def find(self, n, k, arr, x, y, dp):
        if x >= n or y >= n or k < 0:
            return 0
        if x == n - 1 and y == n - 1 and k - arr[x][y] == 0:
            return 1
        if dp[x][y][k] != -1:
            return dp[x][y][k]

        a = self.find(n, k - arr[x][y], arr, x + 1, y, dp)
        b = self.find(n, k - arr[x][y], arr, x, y + 1, dp)

        dp[x][y][k] = a + b
        return dp[x][y][k]

    def numberOfPath(self, n, k, arr):
        dp = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(n)]  # Initialize DP table with -1
        return self.find(n, k, arr, 0, 0, dp)