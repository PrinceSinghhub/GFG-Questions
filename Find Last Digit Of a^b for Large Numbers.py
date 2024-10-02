class Solution:
    def getLastDigit(self, a, b):


        ans = int(a) ** int(b)

        ans = str(ans)

        return int(ans[-1])

ans = Solution()

