# User function Template for python3

class Solution:
    def gameOfXor(self, N, A):
        val = 0
        for i in range(N):
            contribution = (i + 1) * (N - i)
            if contribution % 2 == 1:
                val ^= A[i]
        return val


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().split()))

        ob = Solution()
        print(ob.gameOfXor(N, A))
# } Driver Code Ends