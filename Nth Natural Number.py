class Solution:
    def findNth(self, N):

        ans = 0
        Index = 1
        target = 9
        while (N > 0):
            ans += (Index * (N % target))
            N  = N//target
            Index *= 10


        return ans




t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)



