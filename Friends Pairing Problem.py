# User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        mod = 10 ** 9 + 7
        memo = {}

        def pair(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = pair(i - 1) % mod + (i - 1) * pair(i - 2) % mod
            return memo[i] % mod

        return pair(n)


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends