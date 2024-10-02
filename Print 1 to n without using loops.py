class Solution:
    def printTillN(self, N):
        def printN(N, i):
            if i <= N:
                print(i, end=" ")
                printN(N, i + 1)

        printN(N, 1)


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTillN(N)
        print()
# } Driver Code Ends