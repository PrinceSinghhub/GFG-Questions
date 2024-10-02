class Solution:
    def karyTree(self, k, m):
        mod = 1000000007
        return pow(k, m, mod)


ans = Solution()
k = 2
m = 2
print(ans.karyTree(k,m))