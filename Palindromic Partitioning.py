# User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here

        def ispal(s):
            return s == s[::-1]

        def solve(i, j, string):

            if i >= j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if ispal(string[i:j + 1]):
                return 0

            ans = 10e9

            for k in range(i, j):

                if (ispal(string[i:k + 1])):
                    temp = 1 + solve(k + 1, j, string)
                    ans = min(ans, temp)
            dp[i][j] = ans
            return dp[i][j]

        n = len(string)
        dp = [[-1] * 1001 for i in range(1001)]
        return solve(0, n - 1, string)

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string = input()

        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends