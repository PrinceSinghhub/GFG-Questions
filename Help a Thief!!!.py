class Solution:
    def maxCoins(self, A, B, T, N):
        # code here
        profit = [0] * N
        count = 0
        for i in range(N):
            profit[i] = [B[i], A[i]]
        profit.sort(reverse=True)
        for i in range(N):
            T -= profit[i][1]
            if (T >= 0):
                count += (profit[i][0] * profit[i][1])
                if (T == 0):
                    break
            else:
                T += profit[i][1]
                count += (profit[i][0] * T)
                break
        return count


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        T, N = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        ob = Solution()
        print(ob.maxCoins(A, B, T, N))
# } Driver Code Ends