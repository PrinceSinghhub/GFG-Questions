class Solution:
    def celebrity(self, mat):
        n = len(mat)

        # Step 1: Identify a potential celebrity
        a, b = 0, n - 1
        while a < b:
            if mat[a][b] == 1:
                # a knows b, so a can't be the celebrity, move a forward
                a += 1
            else:
                # a doesn't know b, so b can't be the celebrity, move b backward
                b -= 1

        # a is the potential celebrity
        candidate = a

        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate

