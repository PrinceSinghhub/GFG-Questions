#User function Template for python3

class Solution:
    def TotalCount(self, s):
        # Code here
        n=len(s)
        maxl=100
        dp=[[-1 for i in range(9*maxl+1)] for i in range(maxl)]
        def helper(p,psum):
            if p==n:
                return 1
            if dp[p][psum]!=(-1):
                return dp[p][psum]
            ans=0
            sumd=0
            dp[p][psum]=0
            for i in range(p,n):
                sumd+=int(s[i])
                if sumd>=psum:
                    ans+=helper(i+1,sumd)
            dp[p][psum]=(ans)
            return dp[p][psum]
        return helper(0,0)

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        ans = ob.TotalCount(s)
        print(ans)
# } Driver Code Ends