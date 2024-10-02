import math

class Solution:
    def max_courses(self, n, total, cost):
        dp = [[-1] * (total + 1) for _ in range(n)]
        for i in range(n):
            dp[i][:] = [-1] * (total + 1)

        return self.helper(0, n, total, cost, dp)

    def helper(self, i, n, total, cost, dp):
        if i >= n:
            return 0
        if dp[i][total] != -1:
            return dp[i][total]

        take = 0
        not_take = self.helper(i + 1, n, total, cost, dp)

        if total >= cost[i]:
            take = 1 + self.helper(i + 1, n, total - cost[i] + math.floor(cost[i] * 0.9), cost, dp)

        dp[i][total] = max(take, not_take)
        return dp[i][total]