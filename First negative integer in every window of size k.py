# User function Template for python3

def printFirstNegativeInteger(A, N, K):
    def check(arr):

        for i in arr:
            if i < 0:
                return i

        return 0

    ans = []

    for i in range(N - K + 1):
        temp = A[i:i + K]

        ans.append(check(temp))

    return ans


# using Deque
from collections import deque


def printFirstNegativeInteger(A, N, K):
    d = deque()
    a = []

    for i in range(N):
        while len(d) > 0 and d[0] <= i - K:
            d.popleft()

        if A[i] < 0:
            d.append(i)

        if i >= K - 1:
            if len(d) > 0:
                ele = A[d[0]]
                a.append(ele)
            else:
                a.append(0)

    return a


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends