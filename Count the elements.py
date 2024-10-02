from bisect import bisect_right


class Solution:
    def countElements(self, a, b, n, query, q):
        ans = []
        b.sort()

        for i in range(q):
            idx = bisect_right(b, a[query[i]])
            ans.append(idx)

        return ans