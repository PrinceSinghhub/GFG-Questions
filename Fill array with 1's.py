def minMoves(a, n):
    c, t, p = 0, 0, -1

    for i in range(n):

        if a[i] == 1:

            if p == -1:

                p = i

                c = max(c, t)

                t = 0

            else:

                p = 1

                c = max(c, (t + 1) // 2)

                t = 0

        else:

            t += 1

    c = max(c, t)

    if p == -1:
        c = -1

    return c


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(minMoves(a, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends