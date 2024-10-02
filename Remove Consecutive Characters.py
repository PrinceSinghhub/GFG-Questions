class Solution:
    def removeConsecutiveCharacter(self, s):
       final=''
       s=s[:]+' '
       for i in range(len(s)-1):
         if s[i]!=s[i+1]:
            final+=s[i]
       return final

ans = Solution()
a = "aabb"
print(ans.removeConsecutiveCharacter(a))