class Solution:

    def findSum(self, arr):
        arr = sum(list(set(arr)))
        return arr


ans = Solution()
arr = [5, 5, 5, 5, 5]
print(ans.findSum(arr))