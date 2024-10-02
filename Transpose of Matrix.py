class Solution:

    # Function to find transpose of a matrix.
    def transpose(self, matrix, n):

        arr = []

        for i in range(n):
            temp = []
            for j in range(len(matrix[i])):
                val = matrix[j][i]
                temp.append(val)
            arr.append(temp)

        matrix[:] = arr
        return matrix

ans = Solution()
arr = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
print(ans.transpose(arr,3))