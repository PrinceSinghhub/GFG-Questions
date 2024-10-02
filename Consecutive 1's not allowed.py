class Solution:

    def countStrings(self,n):
        mod=10**9+7
        if n==1:
            return 2;
        if n==2:
            return 3
        a=2;b=3
        for i in range(3,n+1):
            c=(a+b)%mod
            a=b
            b=c
        return b%mod