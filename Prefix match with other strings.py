class Solution:
    def klengthpref(self, arr, n, k, s):
        # return list of words(str) found in the
        c = 0
        if len(s) < k:
            return 0
        p = s[:k]

        for x in arr:
            if x[:k] == p:
                c += 1
        return c