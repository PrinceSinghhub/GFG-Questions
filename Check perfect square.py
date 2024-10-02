class Solution:
    def isPerfectSquare(self, n):
        sqt = int(n ** 0.5)
        print(sqt)
        if n == sqt * sqt:
            return 1
        return 0

ans = Solution()
print(ans.isPerfectSquare(49))