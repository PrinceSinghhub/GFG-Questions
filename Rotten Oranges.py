from collections import deque
class Solution:
    def orangesRotting(self, grid):

        if len(grid) == 0:
            return 0
        row = len(grid)
        coll = len(grid[0])

        total = 0
        days = 0
        count = 0

        queue = deque()

        for i in range(row):
            for j in range(coll):
                if grid[i][j] != 0:
                    total += 1
                if grid[i][j] == 2:
                    queue.append([i, j])

        # print(total)
        # print(queue)

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while len(queue) != 0:
            sizeOfQueue = len(queue)
            count += sizeOfQueue

            while sizeOfQueue > 0:
                data = queue.popleft()
                x = data[0]
                y = data[1]

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0 or nx >= row or ny >= coll or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    queue.append([nx, ny])

                sizeOfQueue -= 1

            if len(queue) != 0:
                days += 1

        if total == count:
            return days
        return -1


#{
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends