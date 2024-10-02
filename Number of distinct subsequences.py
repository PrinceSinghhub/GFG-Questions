class Solution:
    def distinctSubsequences(self, s):
        n = len(s)

    dp = [0] * (n + 1)
    dp[0] = 1
    d = {}

    for i in range(1, n + 1):
        char = s[i - 1]
        dp[i] = dp[i - 1] * 2

        if char in d:
            idx = d[char]
            dp[i] -= dp[idx - 1]
        d[char] = i

    return dp[n] % 1000000007


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.distinctSubsequences(s)
        print(answer)

# } Driver Code Ends