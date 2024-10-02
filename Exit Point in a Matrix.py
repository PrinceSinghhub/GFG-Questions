class Solution:
    def FindExitPoint(self, n, m, matrix):
        pos = 0
        i, j = 0, 0
        pi, pj = -1, -1
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        while 0 <= i < n and 0 <= j < m:
            if matrix[i][j]:
                matrix[i][j] = 0
                pos = (pos + 1) % 4
            pi, pj = i, j
            i += dx[pos]
            j += dy[pos]
        return [pi, pj]