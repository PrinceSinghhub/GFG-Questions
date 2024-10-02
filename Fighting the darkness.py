class Solution:
    def maxDays(self, arr, n):
        arr.sort()
        return arr[n - 1]