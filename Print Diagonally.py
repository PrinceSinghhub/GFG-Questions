def downwardDigonal(N, A):
    # code here

    vis = []

    rans = []

    for i in range(N):

        c = []

        for j in range(N):
            c.append(-1)

        vis.append(c)

    def mark(i, j, N, ans):

        while (i >= 0 and j >= 0 and i < N and j < N):
            ans.append(A[i][j])

            vis[i][j] = 1

            i = i + 1

            j = j - 1

        return ans

    for i in range(N):

        for j in range(N):

            if (vis[i][j] == -1):
                a = mark(i, j, N, [])

                rans += a

    return rans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = []
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n, matrix)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends