class Solution:
    def peakElement(self,arr, n):

        left, right = 0, n-1    #binary search approach

        while left < right:

            mid = (left + right) // 2

            if arr[mid] > arr[mid+1]:

                right = mid

            else:

                left = mid + 1

        return left