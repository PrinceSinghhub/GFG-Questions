class Solution:
    def primeDivision(self, N):
        l = []

        def isprim(nn):
            for t in range(2, int(nn ** (0.5)) + 1):
                if nn % t == 0:
                    return False
            return True

        for t in range(2, N):
            an = isprim(t)
            if an == True:
                l.append(t)
        for t in l:
            for m in l:
                if (t + m) == N:
                    return (t, m)
        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1, end=" ")
        print(p2)
# } Driver Code Ends