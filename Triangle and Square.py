class Solution:
    def countShare(self, B):
        ans = B // 2

        return (ans * (ans - 1)) // 2

ans = Solution()
b = 8
print(ans.countShare(b))