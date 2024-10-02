class Solution:
    def toggleBits(self, N , L , R):
       a = ((1 << R)-1) ^ ((1 << L-1)-1)
       return a^N

ans = Solution()
N = 17
L = 2
R = 3
print(ans.toggleBits(N,L,R))