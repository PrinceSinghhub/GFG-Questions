class Solution:
    def countDigits(self, a, b):
        if a < 0:
            return len(str(abs(a * b)))
        return len(str(a * b))

ans = Solution()
print(ans.countDigits(10,52))