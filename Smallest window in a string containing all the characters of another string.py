# User function Template for python3
# media.net problem
from collections import defaultdict, deque


class Solution:

    def smallestWindow(self, s, p):
        # code here
        start = 0
        length = len(s) + 1
        a = ""
        dic1 = defaultdict(int)
        for i in p:
            dic1[i] += 1

        dic2 = defaultdict(int)
        l = len(p)
        c = 0
        for end in range(len(s)):
            dic2[s[end]] += 1
            if dic1[s[end]] >= dic2[s[end]] and dic2[s[end]] >= 1:
                c += 1
            while c == l:
                m = length
                length = min(length, end - start + 1)
                if length == end - start + 1 and m != length:
                    a = s[start:end + 1]
                dic2[s[start]] -= 1
                if dic1[s[start]] > dic2[s[start]]:
                    c = c - 1
                    if dic2[s[start]] == 0:
                        del dic2[s[start]]
                start = start + 1
        if a != "":
            return a
        return -1

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
    for i in range(t):
        s = str(input())
        p = str(input())
        ob = Solution()
        print(ob.smallestWindow(s, p))
# } Driver Code Ends