class Solution:
    def MaxGold(self, matrix):
# Code here


        n = len(matrix)
        m = len(matrix[0])

        for i in range(n - 2, -1, -1):
            for j in range(0, m):
                if matrix[i][j] != -1:
                    bt = matrix[i + 1][j]
                    br = matrix[i + 1][j + 1] if j + 1 < m else 0
                    bl = matrix[i + 1][j - 1] if j > 0 else 0

                    matrix[i][j] += max([bt, br, bl, 0])

        return max([0] + matrix[0])

ans = Solution()


mat = [[2,5,6],[-1,3,2],[4,-1,5]]
print(ans.MaxGold(mat))

