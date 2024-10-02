class Solution:
    def squaresInMatrix(self, m, n):
       summ=0
       for i in range(min(m,n)):
           summ+=(m-i)*(n-i)
       return summ

ans = Solution()
print(ans.squaresInMatrix(10,5))