from itertools import permutations


class Solution:
    def findNext(self, n):
        con = str(n)

        per = [''.join(i) for i in permutations(con)]

        per = list(sorted(set(per)))

        if per[len(per) - 1] > con:
            return per[per.index(con) + 1]

        return -1
        # your code here


# {
#  Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    n = int(input())
    ob = Solution();
    res = ob.findNext(n)

    if res == -1:
        print("not possible")
    else:
        print(res)