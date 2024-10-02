# User function Template for python3

class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        T = 0;
        B = r - 1;
        L = 0;
        R = c - 1;
        dir = 0;
        ans = []
        while (T <= B and L <= R):
            if (dir == 0):
                for i in range(L, R + 1):
                    ans.append(matrix[T][i])
                T += 1
            elif (dir == 1):
                for i in range(T, B + 1):
                    ans.append(matrix[i][R])
                R -= 1
            elif (dir == 2):
                for i in range(R, L - 1, -1):
                    ans.append(matrix[B][i])
                B -= 1
            elif (dir == 3):
                for i in range(B, T - 1, -1):
                    ans.append(matrix[i][L])
                L += 1
            dir = (dir + 1) % 4
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends