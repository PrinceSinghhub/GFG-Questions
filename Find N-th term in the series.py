# User function Template for python3
class Solution:
    def nthOfSeries(self, n):
        ans = (8 * (n ** 2) + 1)
        return ans

ans = Solution()
print(ans.nthOfSeries(100))