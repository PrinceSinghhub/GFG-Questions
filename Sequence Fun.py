# User function Template for python3

class Solution:
    def NthTerm(self, n):

        # Code here


        if n < 2:
            return 2

        prev = 2

        for i in range(2, n + 1):
            prev = (prev * i) + 1

        return prev % 1000000007

# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.NthTerm(n)
        print(ans)

# } Driver Code Ends