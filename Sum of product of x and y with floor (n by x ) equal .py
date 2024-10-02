class Solution:
    def sumofproduct(self, n):
        ans = 0
        half = 1
        for i in range(1, n + 1):
            half = n // i
            ans += half * i

        return ans

ans = Solution()
print(ans.sumofproduct(20))
