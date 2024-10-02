class Solution:
    def swapElements(self, arr, n):
        for i in range (0,n):
            if ((i+2) < n):
               temp = arr[i]
               arr[i]=arr[i+2]
               arr[i+2] = temp