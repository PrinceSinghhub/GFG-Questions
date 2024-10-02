# User function Template for python3

class Solution:
    def isItPossible(sef, s, t, n, m):
        if n != m: return 0

        i, j = 0, 0

        while (i < n and j < n):
            while (i < n and s[i] == '#'):
                i += 1
            while (j < n and t[j] == '#'):
                j += 1
            if (i == n) ^ (j == n): return 0
            if i < n:
                if s[i] != t[j]:
                    return 0
                elif s[i] == 'B' and j < i:
                    return 0
                elif s[i] == 'A' and j > i:
                    return 0
            i += 1
            j += 1

        return 1


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, T = input().split()
        ob = Solution()
        print(ob.isItPossible(S, T, len(S), len(T)))
# } Driver Code Ends