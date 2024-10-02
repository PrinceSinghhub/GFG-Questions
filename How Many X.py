# User function Template for python3

class Solution:
    def countX(self, L, R, X):
        count = 0
        for i in range(L + 1, R):
            while (i > 0):
                digit = i % 10
                if (digit == X):
                    count += 1
                i = i // 10
        return count


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R, X = map(int, input().strip().split(" "))
        ob = Solution()
        ans = ob.countX(L, R, X)
        print(ans)
        # } Driver Code Ends