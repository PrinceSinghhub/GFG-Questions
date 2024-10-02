class Solution:
   def largestNum(self,n,s):
       if(s > (n*9)):
           return -1
       Res = 0
       for i in range(n):
           if(s >= 9):
               Res *= 10
               Res += 9
               s -= 9
           else:
               Res *= 10
               Res += s
               s -= s
       return Res

ans = Solution()
n = 5
s = 15
print(ans.largestNum(n,s))