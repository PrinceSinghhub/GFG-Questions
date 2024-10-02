# User function Template for python3

class Solution():
    def solve(self, a, b, c):
        if ((a > 2 * (b + c) + 2) or (b > 2 * (a + c) + 2) or (c > 2 * (a + b) + 2)):
            return -1;
        return a + b + c;


# {
# Driver Code Starts
# Initial Template for Python 3

from collections import Counter

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    obj = Solution()
    res = obj.solve(a, b, c)

    print(res)
# } Driver Code Ends