#User function Template for python3

class Solution:

    def countStr(self, n):
        if n == 1:
            return 3
        elif n == 2:
            return 8
        elif n == 3:
            return 19
        else:
            return int(0.5*(n**3 + 3*n + 2))


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends