# User function Template for python3

class Solution:

    def nthRowOfPascalTriangle(self, n):
        mod = 10 ** 9 + 7
        ans = 1
        res = []
        res.append(ans)

        for i in range(1, n):
            # for numenoter calculate
            ans = ans * (n - i)

            # for denominator calculation

            ans = ans // (i)

            res.append(ans % mod)

        return res


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
# } Driver Code Ends