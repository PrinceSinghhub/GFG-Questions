class Solution:
    def search(self, mat, val):
        i = 0
        j = self.n - 1
        while i < self.n and j >= 0:
            if mat[i][j] == val:
                return True
            elif mat[i][j] < val:
                i += 1
            else:
                j -= 1
        return False

    def countPairs(self, mat1, mat2, size, x):
        self.n = size
        count = 0
        for row in mat1:
            for element in row:
                if self.search(mat2, x - element):
                    count += 1
        return count