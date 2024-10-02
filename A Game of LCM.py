import math


class Solution:

    def maxGcd(self, N):

        ans = N

        c = 1

        i = N - 1

        while (i > 1 and c < 4):

            if (math.gcd(ans, i) == 1):
                ans = ans * i

                c += 1

            i -= 1

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = (int)(input())
        ob = Solution()
        print(ob.maxGcd(N))
# } Driver Code Ends