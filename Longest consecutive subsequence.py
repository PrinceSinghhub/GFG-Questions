class Solution:

    # arr[] : the input array
    # N : size of the array arr[]

    # Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self, arr, N):
        # code here

        ds = {}  # Mapping of starts to ends
        de = {}  # Mapping of ends to starts
        m = 1

        for a in arr:
            if a - 1 in de:
                if a + 1 in ds:
                    s = de.pop(a - 1)
                    e = ds.pop(a + 1)
                    ds[s] = e
                    de[e] = s
                    m = max(m, e - s + 1)

                else:
                    s = de.pop(a - 1)
                    de[a] = s
                    ds[s] = a
                    m = max(m, a - s + 1)
            elif a + 1 in ds:
                e = ds.pop(a + 1)
                ds[a] = e
                de[e] = a
                m = max(m, e - a + 1)
            elif a not in ds and a not in de:
                ds[a] = a
                de[a] = a
        return m


# {
#  Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a, n))