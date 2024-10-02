class Solution:
    def revCoding(self, n, m):
        check = (n * (n + 1)) // 2

        if m == check:
            return 1

        return 0

ans = Solution()
print(ans.revCoding(10,55))