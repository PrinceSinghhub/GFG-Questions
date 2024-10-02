# User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        return x | (y & (((1 << (r - l + 1)) - 1) << (l - 1)))
        # code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])

        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends