from collections import defaultdict


class alphanumeric:
    def __init__(self, name, count):
        self.name = name
        self.count = count


class Solution:
    def sortedStrings(self, N, A):
        res = list()
        bucket = defaultdict(int)
        for s in A:
            bucket[s] += 1
        for key in sorted(bucket.keys()):
            res.append(alphanumeric(name=key, count=bucket[key]))
        return res


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        a = []
        for i in range(N):
            x = input()
            a.append(x)
        ob = Solution()
        ans = ob.sortedStrings(N, a)
        for i in ans:
            print(i.name, end=" ")
            print(i.count)
# } Driver Code Ends