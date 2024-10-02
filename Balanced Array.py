class Solution:
    def minValueToBalance(self, a, n):
        mid = (n - 1) // 2

        return abs(sum(a[0:mid + 1]) - sum(a[mid + 1:n]))


# {
#  Driver Code Starts
# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.minValueToBalance(a, n)
    print(ans)