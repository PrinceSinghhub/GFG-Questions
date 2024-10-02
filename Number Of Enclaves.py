#User function Template for python3

from typing import List
from typing import List

class Solution:
    def numberOfEnclaves(self, g: List[List[int]]) -> int:
        r = len(g)
        c = len(g[0])
        visited = [[False for _ in range(c)] for _ in range(r)]

        def bfsofcorner(i, j):
            if i >= r or i < 0 or j >= c or j < 0 or g[i][j] == 0 or visited[i][j]:
                return

            g[i][j] = 0
            visited[i][j] = True

            # Explore neighboring cells
            bfsofcorner(i + 1, j)
            bfsofcorner(i - 1, j)
            bfsofcorner(i, j - 1)
            bfsofcorner(i, j + 1)

        count = 0

        for i in range(r):
            if g[i][0] == 1 and not visited[i][0]:
                bfsofcorner(i, 0)

            if g[i][c - 1] == 1 and not visited[i][c - 1]:
                bfsofcorner(i, c - 1)

        for j in range(c):
            if g[0][j] == 1 and not visited[0][j]:
                bfsofcorner(0, j)

            if g[r - 1][j] == 1 and not visited[r - 1][j]:
                bfsofcorner(r - 1, j)

        for i in range(r):
            for j in range(c):
                if g[i][j] == 1:
                    count += 1

        return count


#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends