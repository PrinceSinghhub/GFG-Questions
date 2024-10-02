class Solution:
    def xorCal(self, k):

        if k == 1:
            return 2

        for i in range(k):
            if i ^ (i + 1) == k:
                return i
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())

        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends