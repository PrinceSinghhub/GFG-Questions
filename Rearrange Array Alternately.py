# User function Template for python3
class Solution:
    ##Complete this function
    # Function to rearrange  the array elements alternately.
    def rearrange(self, arr, n):
        ans_arr = [0] * n
        c = 0
        mid_n = n // 2
        if n % 2 == 1:
            ans_arr[n - 1] = arr[mid_n]

        for i in range(mid_n):
            ans_arr[c] = arr[n - 1 - i]
            c += 1

            ans_arr[c] = arr[i]
            c += 1
        arr[:] = ans_arr[:]
        return ans_arr
        ##Your code here


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
        ob.rearrange(arr, n)

        for i in arr:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":