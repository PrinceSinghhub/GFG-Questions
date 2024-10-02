class Solution:
    def maxIndexDiff(self, A, N):
        diff = 0
        for i in range(N - 1, -1, -1):
            if i >= diff:
                for j in range(0, i):
                    if A[i] >= A[j] and diff <= i - j:
                        diff = i - j
                        break
            else:
                break
        return (diff)

    # {


#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxIndexDiff(arr, n))

        T -= 1


if __name__ == "__main__":
    main()