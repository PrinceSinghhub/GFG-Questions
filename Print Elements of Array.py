class Solution:
    # Just print the space seperated array elements
    def printArray(self, arr, n):
        for i in arr:
            print(i, end=" ")


# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver code
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.printArray(arr, n)
        print()
        tc = tc - 1