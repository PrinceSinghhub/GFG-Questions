# User function Template for python3
class Solution:

    def printUnsorted(self, arr, n):
        # code here
        s = sorted(arr)

        temp = []
        i = 0
        while i < len(arr):
            if arr[i] != s[i]:
                temp.append(i)
            i += 1
        if temp:
            return [min(temp), max(temp)]
        return [0, 0]


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printUnsorted(arr, n)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends