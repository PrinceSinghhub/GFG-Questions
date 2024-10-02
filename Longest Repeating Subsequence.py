class Solution:
    def LongestRepeatingSubsequence(self, str):
        n = len(str)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(n + 1):
                if i > 0 and j > 0:
                    if str[i - 1] == str[j - 1] and i != j:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]
