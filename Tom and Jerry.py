class Solution:
    def numsGame(self, N):
        if N % 2 == 0:
            return '1'
        return '0'


ans = Solution()
print(ans.numsGame(20))