class Solution:
    # Function to sort the array according to difference with given number.
    def sortAbs(self, a, n, k):
        a = sorted(a, key=lambda x: (abs(x - k)))

        return a


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
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(*ob.sortAbs(a, n, k))
