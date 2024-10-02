from typing import List


class Solution:
    def calculate(self, n, m, i, j, ans, temp, grid):

        if (i >= n or j >= m): return

        temp.append(grid[i][j])

        if (i == n - 1 and j == m - 1):
            ans.append(temp[:])

        self.calculate(n, m, i + 1, j, ans, temp, grid)
        self.calculate(n, m, i, j + 1, ans, temp, grid)
        temp.pop()

    def findAllPossiblePaths(self, n: int, m: int, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        temp = []
        self.calculate(n, m, 0, 0, ans, temp, grid)
        return ans
