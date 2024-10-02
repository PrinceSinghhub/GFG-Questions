# User function Template for python3
import math


class Solution:
    def maxStairHeight(self, N):
        # code here
        return int((math.sqrt(1 + 8 * N) - 1) / 2);


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.maxStairHeight(N))
# } Driver Code Ends