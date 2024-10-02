def countOfElements(a, n, x):
    ans = [i for i in a if i <= x]
    return len(ans)


# {
#  Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        print(countOfElements(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()