# User function Template for python3

class Solution:
    def Maximize(self, a, n):
        mod = (10 ** 9 )+ 7
        a.sort()
        ans = 0
        for i in range(n):
            pro = a[i] * i
            ans += pro

        return ans % mod

ans = Solution()
print(ans.Maximize([5, 3, 2, 4, 1],5))