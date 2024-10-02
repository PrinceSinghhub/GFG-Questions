class Solution:
    def count(self, n):
        coins = [3, 5, 10]
        dp = [0] * (n + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, n + 1):
                dp[j] += dp[j - coin]

        return dp[n]