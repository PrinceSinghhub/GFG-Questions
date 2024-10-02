class Solution:
    def numberOfConsecutiveOnes (ob,n):
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n + 1):
            dp[i] = dp[i - 1]
            dp[i] = (dp[i] + dp[i - 2]) % mod
        return (2**n - dp[n]) % mod