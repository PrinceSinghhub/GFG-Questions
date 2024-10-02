class Solution:
    def sequenceCount(self, s, t):
        n = len(s)
        m = len(t)
        MOD = 10 ** 9 + 7

        # Create a 2D DP table to store counts
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: empty string t can be found in any string s once
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, two possibilities:
                # 1. Include current character of both strings
                # 2. Exclude current character of s
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    # If characters don't match, ignore current character of s
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]