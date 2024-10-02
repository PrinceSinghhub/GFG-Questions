# User function Template for python3

class Solution:

    def wineSelling(self, A, N):

        # code here

        buy = []

        sell = []

        for i in range(N):

            if (A[i] > 0):

                buy.append([A[i], i])

            else:

                sell.append([A[i], i])

        ans, i, j, dis = 0, 0, 0, 0

        while (i < len(buy) and j < len(sell)):

            mn = min(buy[i][0], abs(sell[j][0]))

            buy[i][0] -= mn

            sell[j][0] += mn

            dis = abs(buy[i][1] - sell[j][1])

            ans += (dis * mn)

            if (buy[i][0] == 0):
                i += 1

            if (sell[j][0] == 0):
                j += 1

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        Arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.wineSelling(Arr, N)

        print(ans)

# } Driver Code Ends