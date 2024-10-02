class Solution:
    # Complete this function
    # Function to sort the array into a wave-like array.
    def convertToWave(self, arr, N):
        index = 0
        while index < N - 1:
            temp = arr[index]
            arr[index] = arr[index + 1]

            arr[index + 1] = temp

            index += 2
        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().split()]
        ob = Solution()
        ob.convertToWave(A, N)
        for i in A:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()