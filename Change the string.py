class Solution:
    def modify(self, s):

        if s[0].isupper():
            return s.upper()
        else:
            return s.lower()
t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))