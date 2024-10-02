# User function Template for python3
class Solution:

    def findRange(self, a, size):

        dp = [-1] * (size)

        dp[0] = 1 if a[0] == "0" else -1

        for i in range(1, size, 1):

            if a[i] == "0":

                dp[i] = max(dp[i - 1] + 1, 1)

            else:

                dp[i] = max(dp[i - 1] - 1, -1)

        start, end = 0, -1

        mx = 0

        s = -1

        for i in range(n):

            if dp[i] == -1:
                start = i + 1

            if mx < dp[i]:
                s = start

                mx = dp[i]

                end = i

        if s == -1 and end == -1:
            return [-1]

        return [s + 1, end + 1]


# {
# Driver Code Starts
if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        s = input()
        ob = Solution()
        ans = ob.findRange(s, n)
        if len(ans) == 1:
            print(ans[0])
        else:
            print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
# } Driver Code Ends