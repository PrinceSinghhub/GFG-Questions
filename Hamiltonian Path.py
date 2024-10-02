# User function Template for python3
from collections import defaultdict


def chkH(dict1, set1, v, N):
    if v in set1:

        return set1

    else:

        set1.add(v)

        set2 = set()

        set2 = set1.copy()

        for i in dict1[v]:

            set2 = chkH(dict1, set2, i, N)

            if len(set2) == N:

                break

            else:

                set2 = set1.copy()

        return set2


class Solution:

    def check(self, N, M, Edges):

        # code here

        bool1 = False

        dict1 = defaultdict(set)

        for i in range(len(Edges)):
            dict1[Edges[i][0]].add(Edges[i][1])

            dict1[Edges[i][1]].add(Edges[i][0])

        for i in range(1, N + 1):

            set1 = set()

            set1 = chkH(dict1, set1, i, N)

            if len(set1) == N:
                bool1 = True

                break

        return bool1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        Edges = []
        e = list(map(int, input().strip().split()))
        for i in range(M):
            Edges.append([e[2 * i], e[2 * i + 1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends