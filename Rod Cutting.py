class Solution:
    def cutRod(self, price, N):
        dp = [0] * (N+1)  # Initialize dynamic programming array with zeros
        for i in range(1, N+1):
            for j in range(i):
                dp[i] = max(dp[i], price[j] + dp[i-j-1])
        return dp[N]


#{
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends