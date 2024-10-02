#{
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S):
        x=0
        p=len(S)
        c=0
        for i in range(p-1):
            j=i+1
            u1=0
            l1=0
            if(S[i].isupper()):
                u1=u1+1
            else:
                l1=l1+1
            while(j<p):
                if(S[j].isupper()):
                    u1=u1+1
                else:
                    l1=l1+1
                if(u1==l1):
                    c=c+1
                j=j+1
        return c

#{
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends