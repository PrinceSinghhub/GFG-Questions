class Solution:
    def isFit (self,arr, brr, n) :
        #Complete the function
        arr.sort()
        brr.sort()
        for i in range(n):
            if arr[i]>brr[i]:
                return False
        return True