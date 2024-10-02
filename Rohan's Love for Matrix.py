class Solution:
    def firstElement (self, n):
        mod=10**9+7
        res=[1, 1]
        for i in range(n-1):
            res[0],res[1]=(res[0]+res[1])%mod,res[0]
        return res[1]