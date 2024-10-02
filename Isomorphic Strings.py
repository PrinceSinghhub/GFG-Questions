# User function Template for python3

class Solution:

    def areIsomorphic(self, str1, str2):

        n1 = len(str1)
        n2 = len(str2)

        if n1 != n2:
            return False

        dic1 = {}
        dic2 = {}

        for i in range(n1):
            c1 = str1[i]
            c2 = str2[i]
            if c1 not in dic1.keys():
                if c2 in dic2.keys():
                    return False
                else:
                    dic1[c1] = c2
                    dic2[c2] = c1
            else:
                if (c2 not in dic2.keys()) or (dic1[c1] != c2) or (dic2[c2] != c1):
                    return False

        return True


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

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
        if (ob.areIsomorphic(s, p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends