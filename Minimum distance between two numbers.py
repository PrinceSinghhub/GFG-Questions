import sys


class Solution:
    def minDist(self, arr, n, x, y):

        # maintaining list of indices
        x_indices = []
        y_indices = []

        found_x = False
        found_y = False

        for i in range(0, len(arr)):
            if arr[i] == x:
                x_indices.append(i)
                found_x = True

        for j in range(0, len(arr)):
            if arr[j] == y:
                y_indices.append(j)
                found_y = True

        if found_x == False or found_y == False:
            return -1

        min_dis = sys.maxsize

        for i in x_indices:
            for j in y_indices:
                temp = abs(i - j)
                if temp < min_dis:
                    min_dis = temp

        return min_dis


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x, y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))

# } Driver Code Ends