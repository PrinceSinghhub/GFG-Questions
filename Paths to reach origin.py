mod = 1000000007
class Solution:
    def ways(self, n, m):
        dp = [[None] * (m + 1) for _ in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = 1
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n][m] % mod