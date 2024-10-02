import re


class Solution:

    def countWords(self, s):

        ans = 0
        q = s.split()
        print(q)
        for j in q:
            r = j.split('\t')
            print(r)
            for k in r:
                m = k.split('\n')
                print(m)
                for e in m:
                    if len(e) > 0:
                        ans += 1
        return ans
        # ans = (re.split("\t| |\n| |' '", s))
        #
        # return len(ans)


ans = Solution()
a = "a\nhjpfo a\nyo\n"
print(ans.countWords(a))