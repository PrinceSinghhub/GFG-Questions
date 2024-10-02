class Solution:
    def wifiRange(self, N, S, X):
        #code here
        r=0
        count=0
        for i in range(N):
            if S[i]=="1":
                count+=1
                if i-r-1>2*X:
                    return 0
                r=i
            if count==1:
                if r>X:
                    return 0
        if N-r-1>X:
            return 0
        return 1


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        S = input()
        ob = Solution()
        ans = ob.wifiRange(N, S, X)
        if ans:
            print(1)
        else:
            print(0)

# } Driver Code Ends