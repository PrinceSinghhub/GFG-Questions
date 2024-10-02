class Solution:
    def determinant_of_matrix(self, matrix):
        det = 0  # the determinant value will be stored here
        if len(matrix) == 1:
            return matrix[0][0]  # no calculation needed
        elif len(matrix) == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return det
        else:
            for p in range(len(matrix[0])):
                temp_matrix = [row[:p] + row[p + 1:] for row in matrix[1:]]
                det += matrix[0][p] * (-1) ** p * self.determinant_of_matrix(temp_matrix)

            return det