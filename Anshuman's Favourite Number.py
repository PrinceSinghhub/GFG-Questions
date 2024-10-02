class Solution:
    def isValid(self, N):
        if N % 5 == 0:
            return "YES"
        return "NO"

ans = Solution()
print(ans.isValid(10))

