def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        mat = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = int(input())

        temp = 0
        for i in range(n):
            for j in range(n):
                mat[i][j] = line1[temp]
                temp += 1

        print(kthSmallest(mat, n, k))
        T -= 1


if __name__ == "__main__":
    main()