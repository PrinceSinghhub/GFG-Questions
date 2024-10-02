class Solution:
    def select(self, arr, i):
        arr.sort()
        return arr
        # code here

    def selectionSort(self, arr, n):
        return self.select(arr, n)


ans = Solution()
arr = [1,2,8,4,0,90,-1]
print(ans.selectionSort(arr,7))