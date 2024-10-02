# User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        dp = [0] * n
        dp[0] = a[0]

        for i in range(n):
            dp[i] = max(a[i], dp[i - 1] + a[i])

        # print(dp)
        temp = 0
        for i in range(k):
            temp += a[i]

        ans = temp

        for i in range(k, n):
            temp = temp + a[i] - a[i - k]
            ans = max(ans, temp)
            ans = max(ans, temp + dp[i - k])

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends