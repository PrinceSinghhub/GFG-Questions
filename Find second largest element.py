class Solution:
    def print2largest(self, A, N):
        # code here
        A = list(set(A))
        if len(A) < 2:
            return -1

        if len(A) == 2:

            A.sort()
            return A[0]

        else:

            A.sort()
            return A[-2]


# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    ob = Solution()
    print(ob.print2largest(a, n))