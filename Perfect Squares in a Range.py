# User function Template for python3
import math


class Solution:
    def numOfPerfectSquares(self, a, b):
        sqra = int(math.sqrt(a))
        sqrb = int(math.sqrt(b))

        if a == sqra * sqra:
            sqrb += 1

        return sqrb - sqra


# {
#  Driver Code Starts
# Initial Template for Python 3
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())

        ob = Solution()
        print(ob.numOfPerfectSquares(a, b))
# } Driver Code Ends