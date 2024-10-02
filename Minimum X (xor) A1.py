class Solution:
    def minVal(self, a, b):
        ones = sum([int(k) for k in bin(b).replace('0b', '')])
        a = bin(a).replace('0b', '')
        ans = []
        for i in a:
            if i == '0':
                ans += ['0']
            else:
                if ones:
                    ans += ['1']
                    ones -= 1
                else:
                    ans += ['0']
        i = len(ans) - 1
        while ones and i >= 0:
            if ans[i] == '0':
                ans[i] = '1'
                ones -= 1
            i -= 1
        if ones:
            ans = ['1'] * ones + ans
        return int(''.join(ans), 2)


# {
# Driver Code Starts
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
        a = int(input())
        b = int(input())

        ob = Solution()
        print(ob.minVal(a, b))
# } Driver Code Ends