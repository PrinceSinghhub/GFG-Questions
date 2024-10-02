class Solution:

    def findpos(self, n):

        ans = 0
        for i in n:
            if i == "4":
                ans = ans * 2 + 1
            else:
                ans = ans * 2 + 2

        return ans

ans = Solution()
print(ans.findpos("777"))