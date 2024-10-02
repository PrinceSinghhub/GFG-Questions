class Solution:
   def SolveQueris(self, str, query):
       #print(str)
       #print(query)
       result = []
       for q in query:
           left,right = q
           part = str[left - 1:right]#Since counting begins at 1
           #print(part)
           result+=[len(set(part))]
       return result


ans = Solution()
