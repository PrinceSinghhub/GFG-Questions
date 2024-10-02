class Solution:
    def countCamelCase (self,s):

        count = 0
        for i in s:
            ass = ord(i)
            if ass>=65 and ass<=90:
                count+=1

        return count

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print (ob.countCamelCase (s))

