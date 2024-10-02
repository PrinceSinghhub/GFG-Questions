def getCandidate(n, k):
    # complete the function here

    val = k

    while val <= n:
        val *= k

    return val // k


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())

        print(getCandidate(n, k))