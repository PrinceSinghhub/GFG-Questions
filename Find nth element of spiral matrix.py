def findK(arr, m, n, q):
    top, down = 0, m - 1;
    left, right = 0, n - 1;

    while (top <= down and left <= right):

        for j in range(left, right + 1):  ## TOP
            q -= 1
            if q == 0: return arr[top][j];
        top += 1
        for i in range(top, down + 1):  ## RIGHT
            q -= 1
            if q == 0: return arr[i][right]
        right -= 1

        for j in range(right, left - 1, -1):  ## DOWN
            q -= 1
            if q == 0: return arr[down][j]
        down -= 1
        for i in range(down, top - 1, -1):  ## LEFT
            q -= 1
            if q == 0: return arr[i][left]
        left += 1


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findK(matrix, n[0], n[1], n[2]))