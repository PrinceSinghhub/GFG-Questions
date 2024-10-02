# User function Template for python3

class Solution:
    def roundToNearest(self, N):
        k = int(N)
        r = int(k % 10)
        if r > 5:
            return (k - r + 10)
        else:
            return (k - r)


# {
# Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    s = input()
    ob = Solution()
    res = ob.roundToNearest(s)
    print(res)

# } Driver Code Ends