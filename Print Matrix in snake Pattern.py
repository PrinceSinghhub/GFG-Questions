# User function Template for python3

class Solution:

    def snakePattern(self, matrix):
        # code here
        r = c = len(matrix[0])
        res = []

        for i in range(r):
            if i % 2 == 0:
                for j in range(c):
                    res.append(matrix[i][j])
            else:
                for j in range(c - 1, -1, -1):
                    res.append(matrix[i][j])

        return res


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends