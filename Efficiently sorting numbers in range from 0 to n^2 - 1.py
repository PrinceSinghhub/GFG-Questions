# User function Template for python3

class Solution:

    def sort(self, arr, n):
        arr.sort()

        return arr

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        solObj.sort(arr, N)
        for i in arr:
            print(i, end=" ")
        print()

# } Driver Code Ends