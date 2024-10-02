from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        bfs = [(source[0], source[1], 0)]
        dirList = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        n, m = len(grid), len(grid[0])

        seen = {}

        while bfs:
            nxt = []
            for i, j, d in bfs:
                if (i, j) in seen:
                    continue

                if i == destination[0] and j == destination[1]:
                    return d

                seen[(i, j)] = 1

                for dx, dy in dirList:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        nxt.append((x, y, d + 1))

            bfs = nxt

        return -1


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int, input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int, input().strip().split())
        obj = Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends