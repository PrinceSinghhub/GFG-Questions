# User function Template for python3

class Solution:
    def shiftPile(self, N, n):

        def move(k, frm, spare, to):
            nonlocal n
            if k == 0:
                return None
            r = move(k - 1, frm, to, spare)
            if r:
                return r

            n -= 1
            if n == 0:
                return [frm, to]
            return move(k - 1, spare, frm, to)

        return move(N, "1", "2", "3")


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, n = [int(x) for x in input().split()]

        ob = Solution()
        ans = ob.shiftPile(N, n)
        print(ans[0] + " " + ans[1])
# } Driver Code Ends