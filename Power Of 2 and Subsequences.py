class Solution:
    def numberOfSubsequences(ob, N, A):
        d = [True for i in A if not (i & i - 1)]
        return (2 ** sum(d) - 1) % (10 ** 9 + 7)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split(" ")))

        ob = Solution()
        print(ob.numberOfSubsequences(N, A))
# } Driver Code Ends