class Solution:

    def getMoreAndLess(self, arr, n, x):

        l = 0

    m = 0
    for i in arr:
        if i >= x:
            m += 1
        if i <= x:
            l += 1
    return l, m


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMoreAndLess(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1