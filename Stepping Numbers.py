# User function Template for python3


class Solution:
    def steppingNumbers(self, n, m):
        def _solve(v):
            if v > m: return 0
            ans = 1 if n <= v <= m else 0
            last = v % 10
            if last > 0: ans += _solve(v * 10 + last - 1)
            if last < 9: ans += _solve(v * 10 + last + 1)
            return ans

        ans = 0 if n > 0 else 1
        for i in range(1, 10):
            ans += _solve(i)
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        ans = ob.steppingNumbers(N, M);
        print(ans)

# } Driver Code Ends