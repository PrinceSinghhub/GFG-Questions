class Solution:

    def getSingle(self, arr):

        hasmap = {}
        for val in arr:
            if val not in hasmap:
                hasmap[val] = 1
            else:
                hasmap[val] += 1

        for key,val in hasmap.items():
            if val % 2 != 0:
                return key

        return -1
