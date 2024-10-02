class Solution:
    def findIndex(self, a, N, key):

        if a.count(key) == 1:
            return [a.index(key), a.index(key)]

        else:
            first = -1
            last = -1
            for i in range(N):
                if a[i] == key:
                    first = i
                    break

            for i in range(N - 1, -1, -1):
                if a[i] == key:
                    last = i
                    break

            return [first, last]


# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    key = int(input())
    ob = Solution()
    ans = ob.findIndex(a, n, key)
    print(*ans)