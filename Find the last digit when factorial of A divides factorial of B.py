import math


class Solution:
    def lastDigit(self, A, B):
        # code here

        # first = math.factorial(A)
        # last = math.factorial(B)

        # ans = str(last//first)
        # return int(ans[-1])

        ans = 1

        while B > A:
            ans = ans * B
            ans = ans % 10
            B -= 1

        return int(ans)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.lastDigit(A, B))