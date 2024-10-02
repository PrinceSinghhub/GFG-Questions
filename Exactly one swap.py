from collections import Counter as c
class Solution:
    def countStrings(self, s): 
        n = len(s)
        if len(set(s))==len(s):
            return n*(n-1)//2
        z = list(c(s).values())
        ans = 0
        for i in range(len(z)):
            ans += z[i]*sum(z[i+1:])
        return ans+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countStrings(S)
        print(ans)