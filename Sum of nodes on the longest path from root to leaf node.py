import sys
class Solution:
    def __init__(self):
        self.x = -sys.maxsize - 1
        self.mxLvl = 0

    def sumOfLongRootToLeafPath(self, r, lvl=1, s=0):
        if not r:
            return 0

        s += r.data

        if lvl > self.mxLvl:
            self.x = s
            self.mxLvl = lvl
        elif lvl == self.mxLvl:
            self.x = max(self.x, s)

        self.sumOfLongRootToLeafPath(r.left, lvl + 1, s)
        self.sumOfLongRootToLeafPath(r.right, lvl + 1, s)

        return self.x
#{