from collections import Counter


class Solution:

    # Function to sort the array according to frequency of elements.
    # 4 4 5 5 6 : i = 0 return sorted(a, key=lambda x: (-counter[x], x))
    def sortByFreq(self, a, n):
        a.sort()

        check = Counter(a)

        ans = sorted(a, key=lambda x: (- check[x], x))
        return ans


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