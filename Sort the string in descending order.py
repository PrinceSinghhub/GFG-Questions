# User function Template for python3
class Solution:
    def ReverseSort(self, str):
        str = sorted(str)
        ans = "".join(str)
        return ans[::-1]

ans = Solution()
a = "geeks"
print(ans.ReverseSort(a))