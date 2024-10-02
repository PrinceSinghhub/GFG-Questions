class Solution:

    def convert(self, arr, n):
        temp = [arr[i] for i in range(n)]

    # Sort temp array
        temp.sort()

        # create a map
        umap = {}

        # One by one insert elements of sorted
        # temp[] and assign them values from 0
        # to n-1
        val = 0
        for i in range(n):
            umap[temp[i]] = val
            val += 1

        # Convert array by taking positions from umap
        for i in range(n):
            arr[i] = umap[arr[i]]

        return arr


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
