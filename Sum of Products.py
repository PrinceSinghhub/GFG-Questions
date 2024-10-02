#User function Template for python3

class Solution:
    def pairAndSum(self,N, Arr):
        ans = 0
        for i in range(32):
            k = 0
            for j in range(N):
                if (Arr[j] & (1 << i)):
                    k += 1
            ans += (1 << i) * (k * (k - 1) // 2)
        return ans #code here


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends