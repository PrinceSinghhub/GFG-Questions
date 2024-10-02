class Solution:
    def firstNonRepeating(self, arr, n):

        d = {}
        for i in range(n):
            if arr[i] in d.keys():
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        for j in range(n):
            if d[arr[j]] == 1:
                return arr[j]
        return -1

        # for i in arr:
        #     if arr.count(i) == 1:
        #         return i

        # return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

from collections import defaultdict

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
