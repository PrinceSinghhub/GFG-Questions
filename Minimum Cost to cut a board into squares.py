class Solution:
    def minimumCostOfBreaking(self, X, Y, M, N):
        X.sort()
        Y.sort()
        cost = 0
        H_piece, V_piece = 1, 1
        idx_x, idx_y = len(X) - 1, len(Y) - 1

        while idx_x >= 0 and idx_y >= 0:
            if X[idx_x] > Y[idx_y]:
                cost += H_piece * X[idx_x]
                idx_x -= 1
                V_piece += 1
            else:
                cost += V_piece * Y[idx_y]
                idx_y -= 1
                H_piece += 1
        while idx_x >= 0:
            cost += H_piece * X[idx_x]
            idx_x -= 1
            V_piece += 1
        while idx_y >= 0:
            cost += V_piece * Y[idx_y]
            idx_y -= 1
            H_piece += 1
        return cost


# {
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = IntArray().Input(2)
        m = a[0]
        n = a[1]

        tmp = IntArray().Input(a[0] - 1) + IntArray().Input(a[1] - 1)
        X = tmp[:m - 1]
        Y = tmp[m - 1:]

        obj = Solution()
        res = obj.minimumCostOfBreaking(X, Y, m, n)

        print(res)

# } Driver Code Ends