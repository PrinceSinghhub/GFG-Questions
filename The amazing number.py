class Solution:
    def isAmazing(self, n):
        ans = [i for i in range(1, n + 1) if n % i == 0]
        if len(ans) == 3:
            return 1
        return 0

ans = Solution()
print(ans.isAmazing(4))