class Solution:
    def closestNumber(self, N, M):
        con = N
        N = abs(N)

        M = abs(M)
        c = N % M

        if (c < M / 2):
            if (con < 0):
                return -1 * (N - c)
            return (N - c)
        else:
            if (con < 0):
                return -1 * (N + M - c)
            return (N + M - c)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())

        ob = Solution()
        print(ob.closestNumber(N, M))
# } Driver Code Ends