# User function Template for python3

class Solution:

    def isValid(self, board, row, coll, ele):

        for i in range(9):
            if board[i][coll] == ele:
                return False

            if board[row][i] == ele:
                return False

            if board[3 * (row // 3) + i // 3][3 * (coll // 3) + i % 3] == ele:
                return False

        return True

    # Function to find a solved Sudoku.
    def SolveSudoku(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == 0:

                    for ele in range(1, 10):

                        if self.isValid(board, i, j, ele):
                            board[i][j] = ele

                            if self.SolveSudoku(board) == True:
                                return True
                            else:
                                board[i][j] = 0

                    return False

        return True

    # Function to print grids of the Sudoku.
    def printGrid(self, board):

        for i in board:
            for j in i:
                print(j, end=" ")

        # Your code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k += 1

        ob = Solution()

        if (ob.SolveSudoku(grid) == True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t - 1
# } Driver Code Ends