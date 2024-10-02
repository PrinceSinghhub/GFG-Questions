class Solution:
    def canSplit(self, arr):
        sumf,sumh=0,0
        if len(arr)==1:
            return False
        else:
            for i in arr:
                sumf+=i
            for i in arr:
                sumh+=i
                if sumh==sumf-sumh:
                    return True
            return False