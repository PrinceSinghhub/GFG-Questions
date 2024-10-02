class Solution:
    def kPalindrome(self, s, n, k):
        dp = [[0 for _ in range(len(s))] for __ in range(len(s))]
        dp[-1][-1] = 1
        for i in reversed(range(len(dp) - 1)):
            for j in range(i, len(s)):
                dp[i][j] = max(1, dp[i + 1][j], dp[i][j - 1] if j - 1 >= 0 else 0)
                if s[i] == s[j] and i != j:
                    dp[i][j] = max(dp[i][j], 2 + dp[i + 1][j - 1])
        return 1 if len(s) - dp[0][-1] <= k else 0