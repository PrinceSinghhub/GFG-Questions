# User function Template for python3

class Solution:
    def shortestXYDist(self, grid, N, M):
        X_coordinates = []
        Y_coordinates = []
        minDist = N * M
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 'X':
                    X_coordinates.append((row, col))
                elif grid[row][col] == 'Y':
                    Y_coordinates.append((row, col))
        for Row, Col in X_coordinates:
            for row, column in Y_coordinates:
                minDist = min(minDist, abs(Row - row) + abs(Col - column))
                if minDist == 1: break
        return minDist


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        grid = []
        for i in range(N):
            ch = list(map(str, input().split()))
            grid.append(ch)

        ob = Solution()
        print(ob.shortestXYDist(grid, N, M))
# } Driver Code Ends