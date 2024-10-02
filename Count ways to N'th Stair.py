class Solution:
    # Function to count number of ways to reach the nth stair
    # when order does not matter.
    def countWays(self, m):
        dp = [0] * (m + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, m + 1):
            dp[i] = 1 + min(dp[i - 1], dp[i - 2])

        return dp[m]

# Example usage:
# sol = Solution()
# print(sol.countWays(5))  # Replace 5 with any desired input value
