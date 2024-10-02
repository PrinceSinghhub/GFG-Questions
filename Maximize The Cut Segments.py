class Solution:
    def maximizeTheCuts(self, n: int, x: int, y: int, z: int) -> int:
        # Initialize the DP array with negative infinity
        dp = [-float('inf')] * (n + 1)
        dp[0] = 0  # Base case: zero length means zero cuts

        # Fill the DP array
        for i in range(n + 1):
            if dp[i] != -float('inf'):
                if i + x <= n:
                    dp[i + x] = max(dp[i + x], dp[i] + 1)
                if i + y <= n:
                    dp[i + y] = max(dp[i + y], dp[i] + 1)
                if i + z <= n:
                    dp[i + z] = max(dp[i + z], dp[i] + 1)

        # Return the result
        return dp[n] if dp[n] != -float('inf') else 0
