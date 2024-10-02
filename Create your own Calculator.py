class Solution:
    def myCalculator(self, arr):

        def matrixMul(mat, flag, i, arr):
            if flag:
                for j in range(3):
                    mat[j][i], arr[j][-1] = arr[j][-1], mat[j][i]
            res = 0
            res += mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
            res -= mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
            res += mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])

            if flag:
                for j in range(3):
                    mat[j][i], arr[j][-1] = arr[j][-1], mat[j][i]
            return res

        a = []
        for i in range(3):
            a.append(arr[i][:-1])
        p = matrixMul(a, False, -1, arr)
        q = matrixMul(a, True, 0, arr)
        r = matrixMul(a, True, 1, arr)
        s = matrixMul(a, True, 2, arr)
        if p == 0 and (q != 0 or r != 0 or s != 0):
            return 0
        if p == 0 and r == 0 and q == 0 and s == 0:
            return 1
        return [int(q // p), int(r // p), int(s // p)]

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        Arr = []
        for i in range(3):
            arr = input().split()
            for itr in range(4):
                arr[itr] = float(arr[itr])
            Arr.append(arr)

        ob = Solution()
        ans = ob.myCalculator(Arr)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends