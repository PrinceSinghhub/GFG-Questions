class Solution:
    # Function to find the days of buying and selling stock for max profit.
    def stockBuySell(self, A, n):
        buy_days = []

        sell_days = []
        for i in range(n - 1):
            if A[i] < A[i + 1]:
                buy_days.append(i)
                sell_days.append(i + 1)
        L = [[i, j] for i, j in zip(buy_days, sell_days)]

        return L


# {
#  Driver Code Starts
# Initial template for Python

def check(ans, A, p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]] - A[ans[i][0]]
    if (c == p):
        return 1
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        ans = ob.stockBuySell(A, n)
        p = 0
        for i in range(n - 1):
            p += max(0, A[i + 1] - A[i])
        if (len(ans) == 0):
            print("No Profit", end="")
        else:
            print(check(ans, A, p), end="")
        print()
        t -= 1