class Solution:
    def IsPerfect(self, arr, n):
        return arr == arr[::-1]
        # Complete the function


# {
#  Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    if (ob.IsPerfect(arr, n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")