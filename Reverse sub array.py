class Solution:

    def reverseSubArray(self, arr, l, r):
        n = len(arr)
        rev = arr[l - 1:r]

        rev = rev[::-1]
        print(rev)
        ans = arr[0:l-1] + rev + arr[r:n]
        arr[:] = ans
        return arr


ans = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
l = 2
r = 4
print(ans.reverseSubArray(arr,l,r))