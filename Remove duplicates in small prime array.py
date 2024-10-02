class Solution:
    def removeDuplicates(self, arr):

        # code here
        d = dict()
        l = []
        for i in arr:
            if i not in d:
                d[i] = 1
                l.append(i)
        return l