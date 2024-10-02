class Solution:
    def findTime(self, S1, S2):

        mydic = {}
        for i in range(26):
            mydic[S1[i]] = i

        start, step = 0, 0
        for i in range(len(S2)):
            step += abs(mydic[S2[i]] - start)
            start = mydic[S2[i]]
        return step
