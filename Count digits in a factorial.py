import math


class Solution:
    def facDigits(self, N):
        ans = str(math.factorial(N))
        return len(ans)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.facDigits(N))