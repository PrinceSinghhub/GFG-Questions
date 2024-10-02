# User function Template for python3

class Solution:

    def swapBitGame(self, N):

        # code here

        c = 0

        for i in range(39, -1, -1):

            k = N >> i

            if k & 1:
                c += 1

        if c % 2 == 0:
            return 2

        return 1

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.swapBitGame(N))
# } Driver Code Ends