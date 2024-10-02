class Solution:

    def maxStep(self, A, N):
        # Your hode here
        max_step = 0
        step = 0
        for i in range(0, N - 1):
            if A[i + 1] > A[i]:
                step += 1
                if step > max_step:
                    max_step = step
            else:
                step = 0

        return max_step


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(A, N))

        T -= 1


if __name__ == "__main__":
    main()