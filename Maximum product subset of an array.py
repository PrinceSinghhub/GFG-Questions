class Solution:
    def findMaxProduct(self, arr):
        # Write your code here
        n=len(arr)
        d=float("-inf")
        d=max(arr)
        ctzer=0
        if n==1:
            return arr[0]
        ans=1
        res=float("-inf")
        mod=10**9+7
        for i in arr:
            if i==0:

                ctzer+=1
            if i!=0:
                ans=ans*i
            if i<0 and i>res:
                res=i
        if ans<0:
            ans=ans//res
        if ctzer==n:
            return 0
        if d==0 and ans==1:
            return d
        return ans%mod

