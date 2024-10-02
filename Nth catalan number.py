# User function Template for python3

class Solution:
    # Function to find the nth catalan number.
    def findCatalan(self, n):
        if (n == 0):
            return 1
        lst = [0] * (n + 1)
        lst[0] = 1
        for i in range(0, n):
            s = 0
            for j in range(0, n):
                s = s + lst[j] * lst[i - j]
            lst[i + 1] = s
        return lst[n]


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())

        print(Solution().findCatalan(n))

# } Driver Code Ends