#User function Template for python3
class Solution:
    def orientation(self, a, b, c):
        x = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
        if x == 0:
            return 0
        return 1 if x > 0 else 2

    def onSegment(self, a, b, c):
        if (c[0] >= min(a[0], b[0]) and c[0] <= max(a[0], b[0]) and
                c[1] >= min(a[1], b[1]) and c[1] <= max(a[1], b[1])):
            return "true"
        return 'false'

    def doIntersect(self, p1, q1, p2, q2):
        # finding orientation of triplets
        o1 = self.orientation(p1, q1, p2)
        o2 = self.orientation(p1, q1, q2)
        o3 = self.orientation(p2, q2, p1)
        o4 = self.orientation(p2, q2, q1)

        # general case
        if o1 != o2 and o3 != o4:
            return "true"

        # special cases

        # p1, q1, p2 are collinear and p2 lies on segment p1, q1
        if o1 == 0 and self.onSegment(p1, q1, p2):
            return "true"

        # p1, q1, q2 are collinear and q2 lies on segment p1, q1
        if o2 == 0 and self.onSegment(p1, q1, q2):
            return "true"

        # p2, q2, p1 are collinear and p1 lies on segment p2, q2
        if o3 == 0 and self.onSegment(p2, q2, p1):
            return "true"

        # p2, q2, q1 are collinear and q1 lies on segment p2, q2
        if o4 == 0 and self.onSegment(p2, q2, q1):
            return "true"

        return 'false'


#{
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = list(map(int, input().strip().split(" ")))
        S2 = list(map(int, input().strip().split(" ")))
        p1 = []
        q1 = []
        p2 = []
        q2 = []
        p1.append(S1[0])
        p1.append(S1[1])
        q1.append(S1[2])
        q1.append(S1[3])
        p2.append(S2[0])
        p2.append(S2[1])
        q2.append(S2[2])
        q2.append(S2[3])
        ob = Solution()
        ans = ob.doIntersect(p1, q1, p2, q2)
        print(ans)

# } Driver Code Ends