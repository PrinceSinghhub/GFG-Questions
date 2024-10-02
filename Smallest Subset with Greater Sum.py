# User function Template for python3

class Solution:
    def minSubset(self, A, N):
        A.sort()
        c = 0
        Ts = sum(A)
        cs = 0
        for i in range(N - 1, -1, -1):
            cs += A[i]
            Ts -= A[i]
            c += 1
            if Ts < cs:
                return c

        return c


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSubset(A, N)
        print(ans)
# } Driver Code Ends