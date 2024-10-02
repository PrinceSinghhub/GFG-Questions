class Solution:

    def BoundaryTraversal(self, matrix, n, m):
        res = []
        if n == 1:
            for j in range(m):
                res.append(matrix[0][j])
        elif m == 1:
            for i in range(n):
                res.append(matrix[i][0])

        else:
            for i in range(m):
                res.append(matrix[0][i])

            if m > 1:
                for i in range(1, n):
                    res.append(matrix[i][m - 1])

            if n > 1:
                for i in range(m - 2, -1, -1):
                    res.append(matrix[n - 1][i])

                for i in range(n - 2, 0, -1):
                    res.append(matrix[i][0])

        return res

ans = Solution()
arr = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15,16]]

print(ans.BoundaryTraversal(arr,4,4))
