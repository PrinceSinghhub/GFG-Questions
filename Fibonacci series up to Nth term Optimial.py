#User function Template for python3

class Solution:
    def series(self, n):
        ans = []
        mod = 1000000007

        first = 0
        second = 1

        for i in range(n + 1):
            ans.append(first)
            temp = first
            first = second
            second = (temp + second) % mod

        return ans

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends