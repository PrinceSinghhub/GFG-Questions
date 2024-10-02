class Solution:
    def maxSum(self, n):
        if n == 0:
            return 0

        a = max(self.maxSum(n // 2), n // 2)
        b = max(self.maxSum(n // 3), n // 3)
        c = max(self.maxSum(n // 4), n // 4)

        return max((a + b + c), n)