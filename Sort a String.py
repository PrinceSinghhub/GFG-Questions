class Solution:
    def sort(self, s):
        s = sorted(s)

        ans = "".join(s)
        return ans

ans = Solution()
S = "edcab"
print(ans.sort(S))