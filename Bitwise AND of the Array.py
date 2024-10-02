class Solution:
    def count(self, N, A, X):
        ans=sys.maxsize
        m=0
        for i in range(31,-1,-1):
            if((X>>i)&1):
                m|=(1<<i)
                continue
            count=0
            temp=m|(1<<i)
            for i in range(N):
                if((A[i]&temp)==temp):
                    count+=1
            ans=min(ans,N-count)
        return ans

#{
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(N, A, X)
        print(ans)
# } Driver Code Ends