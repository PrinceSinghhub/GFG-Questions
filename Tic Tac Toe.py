class Solution:
    def isValid(self, board):
        oo = False
        xx = True
        xcount = 0
        ycount = 0
        for i in range(9):
            if board[i] == 'X':
                xcount += 1
            if board[i] == 'O':
                ycount += 1
        if xcount - ycount != 1:
            return False

        win = [[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8],
               [0, 3, 6],
               [1, 4, 7],
               [2, 5, 8],
               [0, 4, 8],
               [2, 4, 6]]
        for i in range(8):

            if board[win[i][0]] == 'O' and board[win[i][1]] == 'O' and board[win[i][2]] == 'O':
                oo = True

            if board[win[i][0]] == 'X' and board[win[i][1]] == 'X' and board[win[i][2]] == 'X':
                xx = True

        if (oo):
            return False
        return True


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        board = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.isValid(board)
        if ans:
            print("Valid")
        else:
            print("Invalid")
        tc -= 1