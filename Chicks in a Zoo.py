# User function Template for python3

class Solution:

    def NoOfChicks(self, n):

        # Code here

        if n <= 1:
            return 1

        if n <= 6:

            return 3 * self.NoOfChicks(n - 1)

        elif n == 7:

            return (3 * self.NoOfChicks(n - 1) - 3 * self.NoOfChicks(n - 6))

        else:

            return (3 * self.NoOfChicks(n - 1) - 2 * self.NoOfChicks(n - 6))


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        obj = Solution()
        ans = obj.NoOfChicks(N)
        print(ans)

# } Driver Code Ends