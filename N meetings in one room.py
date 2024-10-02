import numpy as np


class Solution:
    def maximumMeetings(self, n, start, end):
        start = np.array(start)
        ind = start.argsort()
        start = start[ind]
        c = 0
        s = -1
        e = -1
        for i in range(n):
            if end[ind[i]] < e:
                s = start[i]
                e = end[ind[i]]
            elif start[i] > e:
                c = c + 1
                s = start[i]
                e = end[ind[i]]

        return c