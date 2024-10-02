class Solution:
    def minProduct(self, a,k):
        mod = 10 ** 9 + 7

        a.sort()

        mypro = a[0:k]

        ans = 1
        for i in mypro:
            ans *= i
        return ans % mod

ans = Solution()
arr = [1, 2, 3, 4, 5]
k = 2
print(ans.minProduct(arr,k))