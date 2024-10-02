class Solution:
    mod = 10 ** 9 + 7

    def sumSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = int(s[0])
        ans = dp[0]
        for i in range(1, n):
            dp[i] = ((dp[i - 1] * 10) % self.mod + ((int(s[i]) * (i + 1)) % self.mod)) % self.mod
            ans = (ans + dp[i]) % self.mod
        return ans
